from typing import Optional

from djantic import ModelSchema

from . import utils


# class PublisherProjectSchema(ModelSchema):
#     class Config:
#         model = models.PublisherProject


class ItemSchema(ModelSchema):
    class Config:
        model = utils.get_item_model()
        exclude = [
            'boolean_lookup_indexes',
            'children',
            'date_lookup_indexes',
            'datetime_lookup_indexes',
            'float_lookup_indexes',
            'text_lookup_indexes',
        ]


class NestedItemSchema(ModelSchema):
    class Config:
        model = utils.get_item_model()
        exclude = [
            'boolean_lookup_indexes',
            'children',
            'date_lookup_indexes',
            'datetime_lookup_indexes',
            'float_lookup_indexes',
            'parents',
            'text_lookup_indexes',
        ]


class ItemRelationSchema(ModelSchema):
    class Config:
        model = utils.get_item_relation_model()


# class TextLookupIndexSchema(ModelSchema):
#     class Config:
#         model = models.TextLookupIndex


# class FloatLookupIndexSchema(ModelSchema):
#     class Config:
#         model = models.FloatLookupIndex


# class DateLookupIndexSchema(ModelSchema):
#     class Config:
#         model = models.DateLookupIndex


# class DateTimeLookupIndexSchema(ModelSchema):
#     class Config:
#         model = models.DateTimeLookupIndex


# class BooleanLookupIndexSchema(ModelSchema):
#     class Config:
#         model = models.BooleanLookupIndex
