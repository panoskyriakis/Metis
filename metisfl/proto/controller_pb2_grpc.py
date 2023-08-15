# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from metisfl.proto import controller_pb2 as metisfl_dot_proto_dot_controller__pb2
from metisfl.proto import model_pb2 as metisfl_dot_proto_dot_model__pb2
from metisfl.proto import service_common_pb2 as metisfl_dot_proto_dot_service__common__pb2


class ControllerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetHealthStatus = channel.unary_unary(
                '/metisfl.ControllerService/GetHealthStatus',
                request_serializer=metisfl_dot_proto_dot_service__common__pb2.Empty.SerializeToString,
                response_deserializer=metisfl_dot_proto_dot_service__common__pb2.HealthStatusResponse.FromString,
                )
        self.JoinFederation = channel.unary_unary(
                '/metisfl.ControllerService/JoinFederation',
                request_serializer=metisfl_dot_proto_dot_controller__pb2.JoinFederationRequest.SerializeToString,
                response_deserializer=metisfl_dot_proto_dot_controller__pb2.JoinFederationResponse.FromString,
                )
        self.LeaveFederation = channel.unary_unary(
                '/metisfl.ControllerService/LeaveFederation',
                request_serializer=metisfl_dot_proto_dot_controller__pb2.LeaveFederationRequest.SerializeToString,
                response_deserializer=metisfl_dot_proto_dot_service__common__pb2.Ack.FromString,
                )
        self.TrainDone = channel.unary_unary(
                '/metisfl.ControllerService/TrainDone',
                request_serializer=metisfl_dot_proto_dot_controller__pb2.TrainDoneRequest.SerializeToString,
                response_deserializer=metisfl_dot_proto_dot_service__common__pb2.Ack.FromString,
                )
        self.SetInitialModel = channel.unary_unary(
                '/metisfl.ControllerService/SetInitialModel',
                request_serializer=metisfl_dot_proto_dot_model__pb2.Model.SerializeToString,
                response_deserializer=metisfl_dot_proto_dot_service__common__pb2.Ack.FromString,
                )
        self.GetStatistics = channel.unary_unary(
                '/metisfl.ControllerService/GetStatistics',
                request_serializer=metisfl_dot_proto_dot_controller__pb2.GetStatisticsRequest.SerializeToString,
                response_deserializer=metisfl_dot_proto_dot_controller__pb2.GetStatisticsResponse.FromString,
                )
        self.ShutDown = channel.unary_unary(
                '/metisfl.ControllerService/ShutDown',
                request_serializer=metisfl_dot_proto_dot_service__common__pb2.Empty.SerializeToString,
                response_deserializer=metisfl_dot_proto_dot_service__common__pb2.Ack.FromString,
                )


class ControllerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetHealthStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JoinFederation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LeaveFederation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TrainDone(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetInitialModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStatistics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ShutDown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ControllerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetHealthStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHealthStatus,
                    request_deserializer=metisfl_dot_proto_dot_service__common__pb2.Empty.FromString,
                    response_serializer=metisfl_dot_proto_dot_service__common__pb2.HealthStatusResponse.SerializeToString,
            ),
            'JoinFederation': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinFederation,
                    request_deserializer=metisfl_dot_proto_dot_controller__pb2.JoinFederationRequest.FromString,
                    response_serializer=metisfl_dot_proto_dot_controller__pb2.JoinFederationResponse.SerializeToString,
            ),
            'LeaveFederation': grpc.unary_unary_rpc_method_handler(
                    servicer.LeaveFederation,
                    request_deserializer=metisfl_dot_proto_dot_controller__pb2.LeaveFederationRequest.FromString,
                    response_serializer=metisfl_dot_proto_dot_service__common__pb2.Ack.SerializeToString,
            ),
            'TrainDone': grpc.unary_unary_rpc_method_handler(
                    servicer.TrainDone,
                    request_deserializer=metisfl_dot_proto_dot_controller__pb2.TrainDoneRequest.FromString,
                    response_serializer=metisfl_dot_proto_dot_service__common__pb2.Ack.SerializeToString,
            ),
            'SetInitialModel': grpc.unary_unary_rpc_method_handler(
                    servicer.SetInitialModel,
                    request_deserializer=metisfl_dot_proto_dot_model__pb2.Model.FromString,
                    response_serializer=metisfl_dot_proto_dot_service__common__pb2.Ack.SerializeToString,
            ),
            'GetStatistics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatistics,
                    request_deserializer=metisfl_dot_proto_dot_controller__pb2.GetStatisticsRequest.FromString,
                    response_serializer=metisfl_dot_proto_dot_controller__pb2.GetStatisticsResponse.SerializeToString,
            ),
            'ShutDown': grpc.unary_unary_rpc_method_handler(
                    servicer.ShutDown,
                    request_deserializer=metisfl_dot_proto_dot_service__common__pb2.Empty.FromString,
                    response_serializer=metisfl_dot_proto_dot_service__common__pb2.Ack.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'metisfl.ControllerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ControllerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetHealthStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/metisfl.ControllerService/GetHealthStatus',
            metisfl_dot_proto_dot_service__common__pb2.Empty.SerializeToString,
            metisfl_dot_proto_dot_service__common__pb2.HealthStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JoinFederation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/metisfl.ControllerService/JoinFederation',
            metisfl_dot_proto_dot_controller__pb2.JoinFederationRequest.SerializeToString,
            metisfl_dot_proto_dot_controller__pb2.JoinFederationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LeaveFederation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/metisfl.ControllerService/LeaveFederation',
            metisfl_dot_proto_dot_controller__pb2.LeaveFederationRequest.SerializeToString,
            metisfl_dot_proto_dot_service__common__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TrainDone(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/metisfl.ControllerService/TrainDone',
            metisfl_dot_proto_dot_controller__pb2.TrainDoneRequest.SerializeToString,
            metisfl_dot_proto_dot_service__common__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetInitialModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/metisfl.ControllerService/SetInitialModel',
            metisfl_dot_proto_dot_model__pb2.Model.SerializeToString,
            metisfl_dot_proto_dot_service__common__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStatistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/metisfl.ControllerService/GetStatistics',
            metisfl_dot_proto_dot_controller__pb2.GetStatisticsRequest.SerializeToString,
            metisfl_dot_proto_dot_controller__pb2.GetStatisticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ShutDown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/metisfl.ControllerService/ShutDown',
            metisfl_dot_proto_dot_service__common__pb2.Empty.SerializeToString,
            metisfl_dot_proto_dot_service__common__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
