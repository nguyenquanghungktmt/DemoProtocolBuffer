# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contact.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcontact.proto\"\xdb\x01\n\x07\x43ontact\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x14\n\x0ctwitter_name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x13\n\x0bgithub_link\x18\x05 \x01(\t\x12\"\n\x04type\x18\x06 \x01(\x0e\x32\x14.Contact.ContactType\x12\x11\n\timageName\x18\x07 \x01(\t\"8\n\x0b\x43ontactType\x12\x0b\n\x07SPEAKER\x10\x00\x12\r\n\tATTENDANT\x10\x01\x12\r\n\tVOLUNTEER\x10\x02\"&\n\x08Speakers\x12\x1a\n\x08\x63ontacts\x18\x01 \x03(\x0b\x32\x08.Contactb\x06proto3')



_CONTACT = DESCRIPTOR.message_types_by_name['Contact']
_SPEAKERS = DESCRIPTOR.message_types_by_name['Speakers']
_CONTACT_CONTACTTYPE = _CONTACT.enum_types_by_name['ContactType']
Contact = _reflection.GeneratedProtocolMessageType('Contact', (_message.Message,), {
  'DESCRIPTOR' : _CONTACT,
  '__module__' : 'contact_pb2'
  # @@protoc_insertion_point(class_scope:Contact)
  })
_sym_db.RegisterMessage(Contact)

Speakers = _reflection.GeneratedProtocolMessageType('Speakers', (_message.Message,), {
  'DESCRIPTOR' : _SPEAKERS,
  '__module__' : 'contact_pb2'
  # @@protoc_insertion_point(class_scope:Speakers)
  })
_sym_db.RegisterMessage(Speakers)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONTACT._serialized_start=18
  _CONTACT._serialized_end=237
  _CONTACT_CONTACTTYPE._serialized_start=181
  _CONTACT_CONTACTTYPE._serialized_end=237
  _SPEAKERS._serialized_start=239
  _SPEAKERS._serialized_end=277
# @@protoc_insertion_point(module_scope)
