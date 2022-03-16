# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: User.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nUser.proto\"\xb3\x07\n\x04User\x12\n\n\x02id\x18\x02 \x01(\x03\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\tname_show\x18\x04 \x01(\t\x12\x10\n\x08portrait\x18\x05 \x01(\t\x12\x13\n\x0bis_coreuser\x18\x14 \x01(\x05\x12\x10\n\x08level_id\x18\x17 \x01(\x05\x12\x0f\n\x07is_bawu\x18\x19 \x01(\x05\x12\x11\n\tbawu_type\x18\x1a \x01(\t\x12\r\n\x05\x42\x44USS\x18\x1d \x01(\t\x12\x10\n\x08post_num\x18% \x01(\x05\x12\x0e\n\x06tb_age\x18& \x01(\t\x12\x0e\n\x06gender\x18* \x01(\x05\x12!\n\tpriv_sets\x18- \x01(\x0b\x32\x0e.User.PrivSets\x12\x11\n\tis_friend\x18. \x01(\x05\x12&\n\tlikeForum\x18/ \x03(\x0b\x32\x13.User.LikeForumInfo\x12\x13\n\x0bis_guanfang\x18\x34 \x01(\x05\x12\"\n\x07vipInfo\x18= \x01(\x0b\x32\x11.User.UserVipInfo\x12\x0f\n\x07is_fans\x18[ \x01(\x05\x12&\n\x0cnew_god_data\x18\x65 \x01(\x0b\x32\x10.User.NewGodInfo\x12\x19\n\x11is_default_avatar\x18j \x01(\x05\x12\x11\n\ttieba_uid\x18x \x01(\t\x1a\xab\x01\n\x08PrivSets\x12\x10\n\x08location\x18\x01 \x01(\x05\x12\x0c\n\x04like\x18\x02 \x01(\x05\x12\r\n\x05group\x18\x03 \x01(\x05\x12\x0c\n\x04post\x18\x04 \x01(\x05\x12\x0e\n\x06\x66riend\x18\x05 \x01(\x05\x12\x0c\n\x04live\x18\x06 \x01(\x05\x12\r\n\x05reply\x18\x07 \x01(\x05\x12\x19\n\x11\x62\x61zhu_show_inside\x18\x08 \x01(\x05\x12\x1a\n\x12\x62\x61zhu_show_outside\x18\t \x01(\x05\x1a\x35\n\rLikeForumInfo\x12\x12\n\nforum_name\x18\x01 \x01(\t\x12\x10\n\x08\x66orum_id\x18\x02 \x01(\x04\x1a\x97\x01\n\x0bUserVipInfo\x12\x10\n\x08v_status\x18\x01 \x01(\r\x12\x0e\n\x06s_time\x18\x02 \x01(\r\x12\x0e\n\x06\x65_time\x18\x03 \x01(\r\x12\x11\n\text_score\x18\x04 \x01(\r\x12\x0f\n\x07v_level\x18\x05 \x01(\r\x12\x0f\n\x07\x61_score\x18\x06 \x01(\x05\x12\x0f\n\x07n_score\x18\x07 \x01(\r\x12\x10\n\x08icon_url\x18\x08 \x01(\t\x1a\x63\n\nNewGodInfo\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08\x66ield_id\x18\x02 \x01(\r\x12\x12\n\nfield_name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\r\x12\x11\n\ttype_name\x18\x05 \x01(\tb\x06proto3')



_USER = DESCRIPTOR.message_types_by_name['User']
_USER_PRIVSETS = _USER.nested_types_by_name['PrivSets']
_USER_LIKEFORUMINFO = _USER.nested_types_by_name['LikeForumInfo']
_USER_USERVIPINFO = _USER.nested_types_by_name['UserVipInfo']
_USER_NEWGODINFO = _USER.nested_types_by_name['NewGodInfo']
User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {

  'PrivSets' : _reflection.GeneratedProtocolMessageType('PrivSets', (_message.Message,), {
    'DESCRIPTOR' : _USER_PRIVSETS,
    '__module__' : 'User_pb2'
    # @@protoc_insertion_point(class_scope:User.PrivSets)
    })
  ,

  'LikeForumInfo' : _reflection.GeneratedProtocolMessageType('LikeForumInfo', (_message.Message,), {
    'DESCRIPTOR' : _USER_LIKEFORUMINFO,
    '__module__' : 'User_pb2'
    # @@protoc_insertion_point(class_scope:User.LikeForumInfo)
    })
  ,

  'UserVipInfo' : _reflection.GeneratedProtocolMessageType('UserVipInfo', (_message.Message,), {
    'DESCRIPTOR' : _USER_USERVIPINFO,
    '__module__' : 'User_pb2'
    # @@protoc_insertion_point(class_scope:User.UserVipInfo)
    })
  ,

  'NewGodInfo' : _reflection.GeneratedProtocolMessageType('NewGodInfo', (_message.Message,), {
    'DESCRIPTOR' : _USER_NEWGODINFO,
    '__module__' : 'User_pb2'
    # @@protoc_insertion_point(class_scope:User.NewGodInfo)
    })
  ,
  'DESCRIPTOR' : _USER,
  '__module__' : 'User_pb2'
  # @@protoc_insertion_point(class_scope:User)
  })
_sym_db.RegisterMessage(User)
_sym_db.RegisterMessage(User.PrivSets)
_sym_db.RegisterMessage(User.LikeForumInfo)
_sym_db.RegisterMessage(User.UserVipInfo)
_sym_db.RegisterMessage(User.NewGodInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USER._serialized_start=15
  _USER._serialized_end=962
  _USER_PRIVSETS._serialized_start=481
  _USER_PRIVSETS._serialized_end=652
  _USER_LIKEFORUMINFO._serialized_start=654
  _USER_LIKEFORUMINFO._serialized_end=707
  _USER_USERVIPINFO._serialized_start=710
  _USER_USERVIPINFO._serialized_end=861
  _USER_NEWGODINFO._serialized_start=863
  _USER_NEWGODINFO._serialized_end=962
# @@protoc_insertion_point(module_scope)
