# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app_example/grpc/app_example.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"app_example/grpc/app_example.proto\x12\x17\x64sg_example.app_example\x1a\x1bgoogle/protobuf/empty.proto\"$\n\x16QuestionDestroyRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x15\n\x13QuestionListRequest\"R\n\x14QuestionListResponse\x12:\n\x07results\x18\x01 \x03(\x0b\x32).dsg_example.app_example.QuestionResponse\"s\n\x1cQuestionPartialUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x15\n\rquestion_text\x18\x02 \x01(\t\x12\x10\n\x08pub_date\x18\x03 \x01(\t\x12\x1e\n\x16_partial_update_fields\x18\x04 \x03(\t\"F\n\x0fQuestionRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x15\n\rquestion_text\x18\x02 \x01(\t\x12\x10\n\x08pub_date\x18\x03 \x01(\t\"G\n\x10QuestionResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x15\n\rquestion_text\x18\x02 \x01(\t\x12\x10\n\x08pub_date\x18\x03 \x01(\t\"%\n\x17QuestionRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\xf3\x04\n\x12QuestionController\x12_\n\x06\x43reate\x12(.dsg_example.app_example.QuestionRequest\x1a).dsg_example.app_example.QuestionResponse\"\x00\x12T\n\x07\x44\x65stroy\x12/.dsg_example.app_example.QuestionDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x65\n\x04List\x12,.dsg_example.app_example.QuestionListRequest\x1a-.dsg_example.app_example.QuestionListResponse\"\x00\x12s\n\rPartialUpdate\x12\x35.dsg_example.app_example.QuestionPartialUpdateRequest\x1a).dsg_example.app_example.QuestionResponse\"\x00\x12i\n\x08Retrieve\x12\x30.dsg_example.app_example.QuestionRetrieveRequest\x1a).dsg_example.app_example.QuestionResponse\"\x00\x12_\n\x06Update\x12(.dsg_example.app_example.QuestionRequest\x1a).dsg_example.app_example.QuestionResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app_example.grpc.app_example_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QUESTIONDESTROYREQUEST._serialized_start=92
  _QUESTIONDESTROYREQUEST._serialized_end=128
  _QUESTIONLISTREQUEST._serialized_start=130
  _QUESTIONLISTREQUEST._serialized_end=151
  _QUESTIONLISTRESPONSE._serialized_start=153
  _QUESTIONLISTRESPONSE._serialized_end=235
  _QUESTIONPARTIALUPDATEREQUEST._serialized_start=237
  _QUESTIONPARTIALUPDATEREQUEST._serialized_end=352
  _QUESTIONREQUEST._serialized_start=354
  _QUESTIONREQUEST._serialized_end=424
  _QUESTIONRESPONSE._serialized_start=426
  _QUESTIONRESPONSE._serialized_end=497
  _QUESTIONRETRIEVEREQUEST._serialized_start=499
  _QUESTIONRETRIEVEREQUEST._serialized_end=536
  _QUESTIONCONTROLLER._serialized_start=539
  _QUESTIONCONTROLLER._serialized_end=1166
# @@protoc_insertion_point(module_scope)