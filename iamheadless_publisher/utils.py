from .conf import settings
from .loader import get_model


def get_item_model(format='class'):
    string = settings.ITEM_MODEL_CLASS
    if format == 'string':
        return string
    return get_model(string, format)


def get_item_relation_model(format='class'):
    string = settings.ITEM_RELATION_MODEL_CLASS
    if format == 'string':
        return string
    return get_model(string, format)


def get_text_lookup_index_model(format='class'):
    string = settings.TEXT_LOOKUP_INDEX_MODEL_CLASS
    if format == 'string':
        return string
    return get_model(string, format)
