# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: marketplace_transaction/protobuf/offer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from marketplace_transaction.protobuf import rule_pb2 as marketplace__transaction_dot_protobuf_dot_rule__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='marketplace_transaction/protobuf/offer.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n,marketplace_transaction/protobuf/offer.proto\x1a+marketplace_transaction/protobuf/rule.proto\"\x80\x02\n\x05Offer\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06owners\x18\x04 \x03(\t\x12\x0e\n\x06source\x18\x05 \x01(\t\x12\x17\n\x0fsource_quantity\x18\x06 \x01(\x12\x12\x0e\n\x06target\x18\x07 \x01(\t\x12\x17\n\x0ftarget_quantity\x18\x08 \x01(\x12\x12\x14\n\x05rules\x18\t \x03(\x0b\x32\x05.Rule\x12\x1d\n\x06status\x18\n \x01(\x0e\x32\r.Offer.Status\"0\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x08\n\x04OPEN\x10\x01\x12\n\n\x06\x43LOSED\x10\x02\")\n\x0eOfferContainer\x12\x17\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x06.Offerb\x06proto3')
  ,
  dependencies=[marketplace__transaction_dot_protobuf_dot_rule__pb2.DESCRIPTOR,])



_OFFER_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='Offer.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=302,
  serialized_end=350,
)
_sym_db.RegisterEnumDescriptor(_OFFER_STATUS)


_OFFER = _descriptor.Descriptor(
  name='Offer',
  full_name='Offer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Offer.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='Offer.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='Offer.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owners', full_name='Offer.owners', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='Offer.source', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_quantity', full_name='Offer.source_quantity', index=5,
      number=6, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='Offer.target', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_quantity', full_name='Offer.target_quantity', index=7,
      number=8, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rules', full_name='Offer.rules', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Offer.status', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OFFER_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=350,
)


_OFFERCONTAINER = _descriptor.Descriptor(
  name='OfferContainer',
  full_name='OfferContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='OfferContainer.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=393,
)

_OFFER.fields_by_name['rules'].message_type = marketplace__transaction_dot_protobuf_dot_rule__pb2._RULE
_OFFER.fields_by_name['status'].enum_type = _OFFER_STATUS
_OFFER_STATUS.containing_type = _OFFER
_OFFERCONTAINER.fields_by_name['entries'].message_type = _OFFER
DESCRIPTOR.message_types_by_name['Offer'] = _OFFER
DESCRIPTOR.message_types_by_name['OfferContainer'] = _OFFERCONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Offer = _reflection.GeneratedProtocolMessageType('Offer', (_message.Message,), dict(
  DESCRIPTOR = _OFFER,
  __module__ = 'marketplace_transaction.protobuf.offer_pb2'
  # @@protoc_insertion_point(class_scope:Offer)
  ))
_sym_db.RegisterMessage(Offer)

OfferContainer = _reflection.GeneratedProtocolMessageType('OfferContainer', (_message.Message,), dict(
  DESCRIPTOR = _OFFERCONTAINER,
  __module__ = 'marketplace_transaction.protobuf.offer_pb2'
  # @@protoc_insertion_point(class_scope:OfferContainer)
  ))
_sym_db.RegisterMessage(OfferContainer)


# @@protoc_insertion_point(module_scope)
