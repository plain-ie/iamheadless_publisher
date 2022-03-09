import json

from iamheadless_projects.lookups.pagination import ALLOWED_FORMATS

from .. import utils
from ..pydantic_models import ItemSchema, NestedItemSchema

from .index_filters import filter_by_lookup_indexes


def retrieve_item(
        item_id,
        lookup_field='id',
        format='queryset'
        ):

    # --

    Item = utils.get_item_model()
    ItemRelation = utils.get_item_relation_model()

    # --

    if format not in ALLOWED_FORMATS:
        raise ValueError(f'format "{format}" is not supported')

    # --

    if lookup_field != 'id':
        # XXXX fix this
        # .get()
        queryset = Item.objects.all().prefetch_related('parents')
        queryset = filter_by_lookup_indexes(queryset, lookup_field)
        instance = queryset.first()

    else:
        # XXXX fix this
        # .get()
        try:
            instance = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            instance = None

    # --

    if instance is None:
        return None

    if format in ['dict', 'json']:

        parent_relations = ItemRelation.objects.filter(child=instance).distinct()
        pydantic_model = ItemSchema.from_django(instance)

        dict_value = pydantic_model.dict()

        if format == 'dict':
            dict_value['parents'] = {}
            for x in parent_relations:
                if x.status not in dict_value['parents'].keys():
                    dict_value['parents'][x.status] = []
                parent = NestedItemSchema.from_django(x.parent)
                dict_value['parents'][x.status].append(parent.dict())
            return dict_value

        json_value = pydantic_model.json()
        dict_value = json.loads(json_value)

        for x in parent_relations:
            if x.status not in dict_value['parents'].keys():
                dict_value['parents'][x.status] = []
            parent = NestedItemSchema.from_django(x.parent)
            dict_value['parents'][x.status].append(json.loads(parent.json()))

        return json.dumps(dict_value)

    return instance
