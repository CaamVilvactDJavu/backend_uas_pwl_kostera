# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kosts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0bkosts.proto\x12\x05kosts"\xaa\x01\n\x04Kost\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x02\x12\x0e\n\x06rating\x18\x04 \x01(\x02\x12\x0e\n\x06gender\x18\x05 \x01(\t\x12\x15\n\rspecification\x18\x06 \x01(\t\x12\x0c\n\x04rule\x18\x07 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x08 \x01(\t\x12\x10\n\x08\x66\x61\x63ility\x18\t \x01(\t\x12\x11\n\timage_url\x18\n \x01(\t"?\n\x10KostListResponse\x12\x1a\n\x05kosts\x18\x01 \x03(\x0b\x32\x0b.kosts.Kost\x12\x0f\n\x07message\x18\x02 \x01(\t"\x11\n\x0fKostListRequest"\x19\n\x0bKostRequest\x12\n\n\x02id\x18\x01 \x01(\x05":\n\x0cKostResponse\x12\x19\n\x04kost\x18\x01 \x01(\x0b\x32\x0b.kosts.Kost\x12\x0f\n\x07message\x18\x02 \x01(\t"\xab\x01\n\x11KostCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x02\x12\x0e\n\x06rating\x18\x03 \x01(\x02\x12\x0e\n\x06gender\x18\x04 \x01(\t\x12\x15\n\rspecification\x18\x05 \x01(\t\x12\x0c\n\x04rule\x18\x06 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x07 \x01(\t\x12\x10\n\x08\x66\x61\x63ility\x18\x08 \x01(\t\x12\x11\n\timage_url\x18\t \x01(\t"\xb7\x01\n\x11KostUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x02\x12\x0e\n\x06rating\x18\x04 \x01(\x02\x12\x0e\n\x06gender\x18\x05 \x01(\t\x12\x15\n\rspecification\x18\x06 \x01(\t\x12\x0c\n\x04rule\x18\x07 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x08 \x01(\t\x12\x10\n\x08\x66\x61\x63ility\x18\t \x01(\t\x12\x11\n\timage_url\x18\n \x01(\t"\x1f\n\x11KostDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05"%\n\x12KostDeleteResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xbf\x02\n\x05Kosts\x12\x34\n\x07GetKost\x12\x12.kosts.KostRequest\x1a\x13.kosts.KostResponse"\x00\x12=\n\x08GetKosts\x12\x16.kosts.KostListRequest\x1a\x17.kosts.KostListResponse"\x00\x12=\n\nCreateKost\x12\x18.kosts.KostCreateRequest\x1a\x13.kosts.KostResponse"\x00\x12=\n\nUpdateKost\x12\x18.kosts.KostUpdateRequest\x1a\x13.kosts.KostResponse"\x00\x12\x43\n\nDeleteKost\x12\x18.kosts.KostDeleteRequest\x1a\x19.kosts.KostDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "kosts_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_KOST"]._serialized_start = 23
    _globals["_KOST"]._serialized_end = 193
    _globals["_KOSTLISTRESPONSE"]._serialized_start = 195
    _globals["_KOSTLISTRESPONSE"]._serialized_end = 258
    _globals["_KOSTLISTREQUEST"]._serialized_start = 260
    _globals["_KOSTLISTREQUEST"]._serialized_end = 277
    _globals["_KOSTREQUEST"]._serialized_start = 279
    _globals["_KOSTREQUEST"]._serialized_end = 304
    _globals["_KOSTRESPONSE"]._serialized_start = 306
    _globals["_KOSTRESPONSE"]._serialized_end = 364
    _globals["_KOSTCREATEREQUEST"]._serialized_start = 367
    _globals["_KOSTCREATEREQUEST"]._serialized_end = 538
    _globals["_KOSTUPDATEREQUEST"]._serialized_start = 541
    _globals["_KOSTUPDATEREQUEST"]._serialized_end = 724
    _globals["_KOSTDELETEREQUEST"]._serialized_start = 726
    _globals["_KOSTDELETEREQUEST"]._serialized_end = 757
    _globals["_KOSTDELETERESPONSE"]._serialized_start = 759
    _globals["_KOSTDELETERESPONSE"]._serialized_end = 796
    _globals["_KOSTS"]._serialized_start = 799
    _globals["_KOSTS"]._serialized_end = 1118
# @@protoc_insertion_point(module_scope)
