# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Post.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import PbContent_pb2 as PbContent__pb2
from . import SubPostList_pb2 as SubPostList__pb2
from . import Agree_pb2 as Agree__pb2
from . import SimpleForum_pb2 as SimpleForum__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nPost.proto\x1a\x0fPbContent.proto\x1a\x11SubPostList.proto\x1a\x0b\x41gree.proto\x1a\x11SimpleForum.proto\"\x8f\x04\n\x04Post\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05\x66loor\x18\x03 \x01(\r\x12\x0c\n\x04time\x18\x04 \x01(\r\x12\x1b\n\x07\x63ontent\x18\x05 \x03(\x0b\x32\n.PbContent\x12\x17\n\x0fsub_post_number\x18\r \x01(\r\x12\x11\n\tauthor_id\x18\x13 \x01(\x03\x12$\n\rsub_post_list\x18\x0f \x01(\x0b\x32\r.Post.SubPost\x12&\n\tsignature\x18\x15 \x01(\x0b\x32\x13.Post.SignatureData\x12\x15\n\x05\x61gree\x18% \x01(\x0b\x32\x06.Agree\x12 \n\nfrom_forum\x18& \x01(\x0b\x32\x0c.SimpleForum\x12\x0b\n\x03tid\x18. \x01(\x03\x1a;\n\x07SubPost\x12\x0b\n\x03pid\x18\x01 \x01(\x04\x12#\n\rsub_post_list\x18\x02 \x03(\x0b\x32\x0c.SubPostList\x1a\xb4\x01\n\rSignatureData\x12\x14\n\x0csignature_id\x18\x01 \x01(\x05\x12\x13\n\x0b\x66ontKeyName\x18\x02 \x01(\t\x12\x11\n\tfontColor\x18\x03 \x01(\t\x12\x35\n\x07\x63ontent\x18\x04 \x03(\x0b\x32$.Post.SignatureData.SignatureContent\x1a.\n\x10SignatureContent\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\tb\x06proto3')



_POST = DESCRIPTOR.message_types_by_name['Post']
_POST_SUBPOST = _POST.nested_types_by_name['SubPost']
_POST_SIGNATUREDATA = _POST.nested_types_by_name['SignatureData']
_POST_SIGNATUREDATA_SIGNATURECONTENT = _POST_SIGNATUREDATA.nested_types_by_name['SignatureContent']
Post = _reflection.GeneratedProtocolMessageType('Post', (_message.Message,), {

  'SubPost' : _reflection.GeneratedProtocolMessageType('SubPost', (_message.Message,), {
    'DESCRIPTOR' : _POST_SUBPOST,
    '__module__' : 'Post_pb2'
    # @@protoc_insertion_point(class_scope:Post.SubPost)
    })
  ,

  'SignatureData' : _reflection.GeneratedProtocolMessageType('SignatureData', (_message.Message,), {

    'SignatureContent' : _reflection.GeneratedProtocolMessageType('SignatureContent', (_message.Message,), {
      'DESCRIPTOR' : _POST_SIGNATUREDATA_SIGNATURECONTENT,
      '__module__' : 'Post_pb2'
      # @@protoc_insertion_point(class_scope:Post.SignatureData.SignatureContent)
      })
    ,
    'DESCRIPTOR' : _POST_SIGNATUREDATA,
    '__module__' : 'Post_pb2'
    # @@protoc_insertion_point(class_scope:Post.SignatureData)
    })
  ,
  'DESCRIPTOR' : _POST,
  '__module__' : 'Post_pb2'
  # @@protoc_insertion_point(class_scope:Post)
  })
_sym_db.RegisterMessage(Post)
_sym_db.RegisterMessage(Post.SubPost)
_sym_db.RegisterMessage(Post.SignatureData)
_sym_db.RegisterMessage(Post.SignatureData.SignatureContent)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POST._serialized_start=83
  _POST._serialized_end=610
  _POST_SUBPOST._serialized_start=368
  _POST_SUBPOST._serialized_end=427
  _POST_SIGNATUREDATA._serialized_start=430
  _POST_SIGNATUREDATA._serialized_end=610
  _POST_SIGNATUREDATA_SIGNATURECONTENT._serialized_start=564
  _POST_SIGNATUREDATA_SIGNATURECONTENT._serialized_end=610
# @@protoc_insertion_point(module_scope)
