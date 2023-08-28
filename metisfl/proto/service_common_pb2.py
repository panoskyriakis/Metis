# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metisfl/proto/service_common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='metisfl/proto/service_common.proto',
  package='metisfl',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"metisfl/proto/service_common.proto\x12\x07metisfl\x1a\x1fgoogle/protobuf/timestamp.proto\"q\n\x03\x41\x63k\x12\x16\n\x06status\x18\x01 \x01(\x08R\x06status\x12\x38\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12\x18\n\x07message\x18\x03 \x01(\tR\x07message\"F\n\x14HealthStatusResponse\x12.\n\x06status\x18\x01 \x01(\x0e\x32\x16.metisfl.ServingStatusR\x06status\"\x18\n\x16GetHealthStatusRequest\"9\n\x17GetHealthStatusResponse\x12\x1e\n\x03\x61\x63k\x18\x01 \x01(\x0b\x32\x0c.metisfl.AckR\x03\x61\x63k\"\x07\n\x05\x45mpty\"2\n\x10ShutDownResponse\x12\x1e\n\x03\x61\x63k\x18\x01 \x01(\x0b\x32\x0c.metisfl.AckR\x03\x61\x63k*:\n\rServingStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SERVING\x10\x01\x12\x0f\n\x0bNOT_SERVING\x10\x02\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_SERVINGSTATUS = _descriptor.EnumDescriptor(
  name='ServingStatus',
  full_name='metisfl.ServingStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_SERVING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=413,
  serialized_end=471,
)
_sym_db.RegisterEnumDescriptor(_SERVINGSTATUS)

ServingStatus = enum_type_wrapper.EnumTypeWrapper(_SERVINGSTATUS)
UNKNOWN = 0
SERVING = 1
NOT_SERVING = 2



_ACK = _descriptor.Descriptor(
  name='Ack',
  full_name='metisfl.Ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='metisfl.Ack.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='metisfl.Ack.timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timestamp', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='metisfl.Ack.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='message', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=193,
)


_HEALTHSTATUSRESPONSE = _descriptor.Descriptor(
  name='HealthStatusResponse',
  full_name='metisfl.HealthStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='metisfl.HealthStatusResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=265,
)


_GETHEALTHSTATUSREQUEST = _descriptor.Descriptor(
  name='GetHealthStatusRequest',
  full_name='metisfl.GetHealthStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=267,
  serialized_end=291,
)


_GETHEALTHSTATUSRESPONSE = _descriptor.Descriptor(
  name='GetHealthStatusResponse',
  full_name='metisfl.GetHealthStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='metisfl.GetHealthStatusResponse.ack', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ack', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=293,
  serialized_end=350,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='metisfl.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=359,
)


_SHUTDOWNRESPONSE = _descriptor.Descriptor(
  name='ShutDownResponse',
  full_name='metisfl.ShutDownResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='metisfl.ShutDownResponse.ack', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ack', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=411,
)

_ACK.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_HEALTHSTATUSRESPONSE.fields_by_name['status'].enum_type = _SERVINGSTATUS
_GETHEALTHSTATUSRESPONSE.fields_by_name['ack'].message_type = _ACK
_SHUTDOWNRESPONSE.fields_by_name['ack'].message_type = _ACK
DESCRIPTOR.message_types_by_name['Ack'] = _ACK
DESCRIPTOR.message_types_by_name['HealthStatusResponse'] = _HEALTHSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['GetHealthStatusRequest'] = _GETHEALTHSTATUSREQUEST
DESCRIPTOR.message_types_by_name['GetHealthStatusResponse'] = _GETHEALTHSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['ShutDownResponse'] = _SHUTDOWNRESPONSE
DESCRIPTOR.enum_types_by_name['ServingStatus'] = _SERVINGSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ack = _reflection.GeneratedProtocolMessageType('Ack', (_message.Message,), {
  'DESCRIPTOR' : _ACK,
  '__module__' : 'metisfl.proto.service_common_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.Ack)
  })
_sym_db.RegisterMessage(Ack)

HealthStatusResponse = _reflection.GeneratedProtocolMessageType('HealthStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHSTATUSRESPONSE,
  '__module__' : 'metisfl.proto.service_common_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.HealthStatusResponse)
  })
_sym_db.RegisterMessage(HealthStatusResponse)

GetHealthStatusRequest = _reflection.GeneratedProtocolMessageType('GetHealthStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETHEALTHSTATUSREQUEST,
  '__module__' : 'metisfl.proto.service_common_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.GetHealthStatusRequest)
  })
_sym_db.RegisterMessage(GetHealthStatusRequest)

GetHealthStatusResponse = _reflection.GeneratedProtocolMessageType('GetHealthStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETHEALTHSTATUSRESPONSE,
  '__module__' : 'metisfl.proto.service_common_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.GetHealthStatusResponse)
  })
_sym_db.RegisterMessage(GetHealthStatusResponse)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'metisfl.proto.service_common_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.Empty)
  })
_sym_db.RegisterMessage(Empty)

ShutDownResponse = _reflection.GeneratedProtocolMessageType('ShutDownResponse', (_message.Message,), {
  'DESCRIPTOR' : _SHUTDOWNRESPONSE,
  '__module__' : 'metisfl.proto.service_common_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.ShutDownResponse)
  })
_sym_db.RegisterMessage(ShutDownResponse)


# @@protoc_insertion_point(module_scope)
