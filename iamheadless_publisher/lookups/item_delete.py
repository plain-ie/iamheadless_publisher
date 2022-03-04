from .. import utils


def delete_item(
        item_ids
        ):

    # --

    Item = utils.get_item_model()

    # --

    if isinstance(item_ids, list) is False:
        item_ids = [item_ids, ]

    # --

    Item.objects.filter(id__in=item_ids).delete()

    # --

    return None
