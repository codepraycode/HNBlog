from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import StoryItemModel
from helpers.admin import BaseItemAdmin

# Register your models here.


@admin.register(StoryItemModel)
class StoryItemAdmin(admin.ModelAdmin, BaseItemAdmin):
    
    
    list_display = (
        # 'item_type',
        'title',
        'url',
        'author',
        'comments',
        # 'score',
    )

    search_fields = (
        'author',
        'title',
    )

    fieldsets = (
        (_("Author"), {
            "fields": (
                'by',
            ),
        }),
        (_("Meta"), {
            "fields": (
                'deleted',
                'dead',
                '_type',
                'time',
            ),
        }),
        (_("Content"), {
            "fields": (
                'title',
                'url',
                'descendants',
                'score',
            ),
        }),
    )
    
    def comments(self, obj):
        return obj.descendants
