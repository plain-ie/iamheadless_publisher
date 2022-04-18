from iamheadless_projects.lookups.pagination import ALLOWED_FORMATS, pagination

from .. import utils
from ..pydantic_models import ItemSchema

from .index_filters import filter_by_lookup_indexes


def retrieve_items(
        count='__all__',
        format='queryset',
        index_filters=None,
        item_ids=None,
        item_types=None,
        project_ids=None,
        page=1,
        published=None,
        unpublished=None,
        tenant_ids=None,
        ordering='-created_at',
        item_pydantic_model=None,
        ):

    # --

    Item = utils.get_item_model()

    # --

    if item_pydantic_model is None:
        item_pydantic_model = ItemSchema

    if format not in ALLOWED_FORMATS:
        raise ValueError(f'format "{format}" is not supported')

    if isinstance(index_filters, list) is False and index_filters is not None:
        index_filters = [index_filters,]

    if isinstance(item_ids, list) is False and item_ids is not None:
        item_ids = [item_ids, ]

    if isinstance(item_types, list) is False and item_types is not None:
        item_types = [item_types, ]

    if isinstance(project_ids, list) is False and project_ids is not None:
        project_ids = [project_ids, ]

    if isinstance(tenant_ids, list) is False and tenant_ids is not None:
        tenant_ids = [tenant_ids, ]

    if published not in [None, True]:
        raise ValueError('published value must be one of None, True')

    if unpublished not in [None, True]:
        raise ValueError('unpublished value must be one of None, True')

    # --

    queryset = Item.objects.all().prefetch_related('parents')

    if item_ids is not None:
        queryset = queryset.filter(id__in=item_ids)

    if item_types is not None:
        queryset = queryset.filter(item_type__in=item_types)

    if project_ids is not None:
        queryset = queryset.filter(project_id__in=project_ids)

    if tenant_ids is not None:
        queryset = queryset.filter(tenant_id__in=tenant_ids)

    if index_filters is not None:
        for x in index_filters:
            queryset = filter_by_lookup_indexes(queryset, x)

    queryset = queryset.order_by(ordering).distinct()

    # --

    paginated_data = pagination(queryset, page, count, item_pydantic_model)

    if format == 'dict':
        return paginated_data.dict

    if format == 'json':
        return paginated_data.json

    return paginated_data
