from django.db import models

from iamheadless_projects import utils as iamheadless_projects_utils


Project = iamheadless_projects_utils.get_project_model(format='string')
Tenant = iamheadless_projects_utils.get_tenant_model(format='string')


class PublisherProject(models.Model):
    project = models.OneToOneField(Project, related_name='publishing_app', on_delete=models.CASCADE)


class Item(models.Model):
    data = models.JSONField(default=dict, blank=True, null=True)
    item_type = models.CharField(max_length=4096, db_index=True)
    project = models.ForeignKey(Project, related_name='iamheadless_publisher_items', on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, related_name='iamheadless_publisher_items', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ItemRelation(models.Model):
    child = models.ForeignKey(Item, related_name='parents', on_delete=models.CASCADE)
    parent = models.ForeignKey(Item, related_name='children', on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TextLookupIndex(models.Model):
    item = models.ForeignKey(Item, related_name='text_lookup_indexes', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=4096, db_index=True)
    value = models.CharField(max_length=4096)


class FloatLookupIndex(models.Model):
    item = models.ForeignKey(Item, related_name='float_lookup_indexes', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=4096, db_index=True)
    value = models.DecimalField(max_digits=100000000000000000000, decimal_places=100000000000000000000)


class DateLookupIndex(models.Model):
    item = models.ForeignKey(Item, related_name='date_lookup_indexes', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=4096, db_index=True)
    value = models.DateField()


class DateTimeLookupIndex(models.Model):
    item = models.ForeignKey(Item, related_name='datetime_lookup_indexes', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=4096, db_index=True)
    value = models.DateTimeField()


class BooleanLookupIndex(models.Model):
    item = models.ForeignKey(Item, related_name='boolean_lookup_indexes', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=4096, db_index=True)
    value = models.BooleanField(default=None)
