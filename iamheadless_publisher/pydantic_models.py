from djantic import ModelSchema

from . import utils


# class PublisherProjectSchema(ModelSchema):
#     class Config:
#         model = models.PublisherProject


class ItemSchema(ModelSchema):
    class Config:
        model = utils.get_item_model()


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
