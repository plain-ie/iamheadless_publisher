from django.contrib import admin

from . import models


class ItemRelationInline(admin.StackedInline):
    model = models.ItemRelation
    fk_name = 'child'
    raw_id_fields = ['parent', 'child']
    extra = 0


class ItemAdmin(admin.ModelAdmin):
   raw_id_fields = ['project', 'tenant']
   inlines = [ItemRelationInline]


class TextLookupIndexAdmin(admin.ModelAdmin):
   raw_id_fields = ['item']


admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.TextLookupIndex, TextLookupIndexAdmin)
