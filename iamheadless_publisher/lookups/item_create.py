from iamheadless_projects.lookups.pagination import ALLOWED_FORMATS

from .. import utils
from ..pydantic_models import ItemSchema


def create_item(
        data={},
        format='queryset',
        item_pydantic_model=None
        ):

    # --

    Item = utils.get_item_model()
    ItemRelation = utils.get_item_relation_model()

    # --

    if item_pydantic_model is None:
        item_id = ItemSchema

    if format not in ALLOWED_FORMATS:
        raise ValueError(f'format "{format}" is not supported')

    # --

    parent_relations = data.pop('parent_relations', {})
    indexes = data.pop('indexes', {})

    # --

    instance = Item.objects.create(**data)
    item_id = instance.id

    # --

    for key in indexes.keys():

        model = None
        new_index_ids = []

        if key == 'text':
            model = utils.get_text_lookup_index_model()
            for value in indexes[key]:
                new_index = model.objects.create(
                    item_id=item_id,
                    field_name=value['field_name'],
                    value=value['value']
                )
                new_index_ids.append(new_index.id)

            model.objects.filter(
                item_id=item_id
            ).exclude(
                id__in=new_index_ids
            ).delete()

        if key == 'float':
            pass

        if key == 'date':
            pass

        if key == 'datetime':
            pass

    # --

    instance = Item.objects.get(id=item_id)

    if format in ['dict', 'json']:

        pydantic_model = item_pydantic_model.from_django(instance)

        if format == 'dict':
            return pydantic_model.dict()

        return pydantic_model.json()

    return instance
