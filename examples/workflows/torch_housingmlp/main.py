import argparse
import json
import os
import random
import torch

import scipy.stats

import pandas as pd
import numpy as np

from housing_mlp import HousingMLP
from metisfl.model.torch.torch_model import MetisModelTorch
from metisfl.common.config import FederationEnvironment
from metisfl.driver.driver_session import DriverSession
from metisfl.model.model_dataset import ModelDatasetRegression
from torch.utils.data import DataLoader

class EnvGen(object):

    def __init__(self, template_filepath=None):
        self.template_filepath = template_filepath
        if not template_filepath:
            self.template_filepath = os.path.join(
                os.path.dirname(__file__),
                "../fedenv_templates/template.yaml")

    def generate_localhost(self,
                           federation_rounds=10,
                           learners_num=10,
                           gpu_devices=[-1],
                           gpu_assignment="round_robin",
                           without_ssl=True):   
        fstream = open(self.template_filepath).read()
        loaded_yaml = yaml.load(fstream, Loader=yaml.SafeLoader)
        loaded_yaml["TerminationSignals"]["FederationRounds"] = federation_rounds
        if without_ssl:
            loaded_yaml["Controller"]["SSLConfig"] = None
        learner_template = loaded_yaml["Learners"][0]
        if without_ssl:
            learner_template["SSLConfig"] = None
        all_learners = []
        gpu_devices_iter = itertools.cycle(gpu_devices)
        if gpu_assignment != "round_robin":
            raise RuntimeError("Only Round-Robin assignment is currently supported.")
        for k in range(learners_num):
            new_learner = copy.deepcopy(learner_template)
            new_learner["CudaDevices"] = [int(next(gpu_devices_iter))]
            new_learner["GRPCServer"]["Port"] = \
                int(learner_template["GRPCServer"]["Port"] + k)
            all_learners.append(new_learner)
        loaded_yaml["Learners"] = all_learners
        # federation_environment = FederationEnvironment(loaded_yaml)
        # return federation_environment


if __name__ == "__main__":

    script_cwd = os.path.dirname(__file__)
    print("Script current working directory: ", script_cwd, flush=True)
    parser = argparse.ArgumentParser()
    parser.add_argument("--communication_protocol",
                        default="Synchronous", type=str)
    parser.add_argument("--federation_rounds", default=10, type=int)
    parser.add_argument("--learners_num", default=10, type=int)
    parser.add_argument("--train_samples_per_learner", default=10, type=int)
    parser.add_argument("--test_samples", default=10, type=int)
    parser.add_argument("--nn_params_per_layer", default=10, type=int)
    parser.add_argument("--nn_hidden_layers_num", default=0, type=int)
    parser.add_argument("--data_type", default="float32", type=str)
    parser.add_argument("--template_filepath", default=None, type=str)

    args = parser.parse_args()
    print(args, flush=True)

    """ Load training and test data. """
    required_training_samples = int(
        args.learners_num * args.train_samples_per_learner)
    total_required_samples = required_training_samples + int(args.test_samples)
    housing_np = pd.read_csv(
        script_cwd + "/housing_data.csv").to_numpy()
    housing_np = housing_np[~np.isnan(housing_np).any(axis=1)]

    total_rows = len(housing_np)
    if total_required_samples > total_rows:
        diff = total_required_samples - total_rows
        for i in range(diff):
            # Append random row from the original set of rows.
            housing_np = np.vstack(
                [housing_np,
                 housing_np[random.randrange(total_rows)]])

    np.random.shuffle(housing_np)
    train_data, test_data = housing_np[:required_training_samples], housing_np[-args.test_samples:]
    # First n-1 are input features, last feature is prediction/output feature.
    x_train, y_train = train_data[:, :-1], train_data[:, -1:]
    x_test, y_test = test_data[:, :-1], test_data[:, -1:]

    x_chunks, y_chunks = np.split(x_train, args.learners_num), np.split(
        y_train, args.learners_num)
    
    datasets_path = os.path.join(script_cwd, "datasets/")
    if not os.path.exists(datasets_path):
        os.makedirs(datasets_path)
    
    test_dataset_path = os.path.join(datasets_path, "test.npz")
    np.savez(test_dataset_path, x=x_test, y=y_test)
    
    train_dataset_fps, test_dataset_fps = [], []        
    for cidx, (x_chunk, y_chunk) in enumerate(zip(x_chunks, y_chunks)):
        learner_train_datset_path = os.path.join(datasets_path,
                 "train_{}.npz".format(cidx))
        np.savez(learner_train_datset_path, x=x_chunk, y=y_chunk)
        train_dataset_fps.append(learner_train_datset_path)
        test_dataset_fps.append(test_dataset_path)

    def dataset_recipe_fn(dataset_fp):
        dataset = np.load(dataset_fp)
        features, prices = dataset['x'], dataset['y']
        features = np.vstack(features)
        prices = np.concatenate(prices)
        mode_values, mode_counts = scipy.stats.mode(prices)
        if np.all((mode_counts == 1)):
            mode_val = np.max(prices)
        else:
            mode_val = mode_values[0]

        features_tensor, prices_tensor = \
            torch.from_numpy(features).to(torch.float64), \
            torch.from_numpy(prices).to(torch.float64)
        tensor_dataset = torch.utils.data.TensorDataset(
            features_tensor, prices_tensor)
        data_loader = torch.utils.data.DataLoader(tensor_dataset)

        model_dataset = ModelDatasetRegression(
            x=data_loader, size=len(prices),
            min_val=np.min(prices), max_val=np.max(prices),
            mean_val=np.mean(prices), median_val=np.median(prices),
            mode_val=mode_val, stddev_val=np.std(prices))
        return model_dataset

    # Define the network.
    nn_model = HousingMLP()
    nn_model.fit(dataset_recipe_fn(datasets_path + "/train_1.npz").get_x(), epochs=10)

    # Wrap the model.
    nn_model = MetisModelTorch(nn_model)

    driver_session = DriverSession(fed_env=EnvGen().template_filepath,
                                   model=nn_model,
                                   train_dataset_fps=train_dataset_fps,
                                   train_dataset_recipe_fn=dataset_recipe_fn,
                                   validation_dataset_recipe_fn=dataset_recipe_fn,
                                   test_dataset_fps=test_dataset_fps,
                                   test_dataset_recipe_fn=dataset_recipe_fn)
    driver_session.initialize_federation()
    driver_session.monitor_federation()
    driver_session.shutdown_federation()
    statistics = driver_session.get_federation_statistics()

    with open(os.path.join(script_cwd, "experiment.json"), "w+") as fout:
        print("Execution File Output Path:", fout.name, flush=True)
        json.dump(statistics, fout, indent=4)
