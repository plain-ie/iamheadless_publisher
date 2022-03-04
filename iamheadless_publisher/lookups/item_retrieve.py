from iamheadless_projects.lookups.pagination import ALLOWED_FORMATS

from .. import utils
from ..pydantic_models import ItemSchema

from .index_filters import filter_by_lookup_indexes


def retrieve_item(
        item_id,
        lookup_field='id',
        format='queryset'
        ):

    # --

    Item = utils.get_item_model()

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

        pydantic_model = ItemSchema.from_django(instance)

        if format == 'dict':
            return pydantic_model.dict()

        return pydantic_model.json()

    return instance
