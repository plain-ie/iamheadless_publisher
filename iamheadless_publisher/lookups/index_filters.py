def index_filter_related_name(index_filter):
    return index_filter.split('__')[0]


def index_filter_condition(index_filter):
    return index_filter.split('||')[0]


def index_filter_field(index_filter):
    return index_filter.split('||')[1]


def index_filter_value(index_filter):
    try:
        return index_filter.split('||')[2]
    except IndexError:
        return None


def index_filter_value_condition(value):
    parts = value.split('__')
    if len(parts) == 2:
        return parts[0]
    return None


def filter_by_lookup_indexes(queryset, index_filter):

    filter = index_filter_condition(index_filter)
    related_name = index_filter_related_name(index_filter)
    field = index_filter_field(index_filter)
    value = index_filter_value(index_filter)

    value_condition = index_filter_value_condition(value)
    if value_condition is None:
        value_condition = ''
    else:
        value_condition = f'__{value_condition}'
        value = value.split('__')[1]

    queryset = queryset.filter(
        **{
            filter: field,
            f'{related_name}__value{value_condition}': value
        }
    ).prefetch_related(
        related_name
    )

    return queryset
