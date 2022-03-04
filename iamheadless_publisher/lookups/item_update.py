from django.db import transaction

from iamheadless_projects.lookups.pagination import ALLOWED_FORMATS

from .. import utils
from ..pydantic_models import ItemSchema


def update_item(
        item_id,
        data={},
        format='queryset'
        ):

    # --

    Item = utils.get_item_model()
    ItemRelation = utils.get_item_relation_model()

    # --

    if format not in ALLOWED_FORMATS:
        raise ValueError(f'format "{format}" is not supported')

    # --

    parent_relations = data.pop('parent_relations', {})
    indexes = data.pop('indexes', {})

    # --

    with transaction.atomic():

        # XXXX TODO
        # Fix this as it takes too much og juice
        # Must have .get()

        Item.objects.filter(id=item_id).update(**data)

        new_parent_relation_ids = []

        for key in parent_relations.keys():
            for x in parent_relations[key]:

                relation_instance = ItemRelation.objects.create(
                    parent_id=x['item_id'],
                    child_id=item_id,
                    status=x['status'],
                )

                new_parent_relation_ids.append(relation_instance.id)

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

            if key == 'bool':
                pass

        ItemRelation.objects.filter(
            child_id=item_id
        ).exclude(
            id__in=new_parent_relation_ids
        ).delete()

    # --

    instance = Item.objects.get(id=item_id)

    # --

    if format in ['dict', 'json']:

        pydantic_model = ItemSchema.from_django(instance)

        if format == 'dict':
            return pydantic_model.dict()

        return pydantic_model.json()

    return instance
