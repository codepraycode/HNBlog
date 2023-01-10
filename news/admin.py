from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import StoryItemModel, CommentItemModel
from helpers.admin import BaseItemAdmin

# Register your models here.


@admin.register(StoryItemModel)
class StoryItemAdmin(admin.ModelAdmin, BaseItemAdmin):
    
    
    list_display = (
        # 'itemtype',
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
                'hnId',
                'deleted',
                'dead',
                'type',
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
    
@admin.register(CommentItemModel)
class CommentItemAdmin(admin.ModelAdmin, BaseItemAdmin):
    
    
    list_display = (
        'text',
        'parent',
        'author',
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
                'hnId',
                'deleted',
                'dead',
                'type',
                'time',
            ),
        }),
        (_("Content"), {
            "fields": (
                'text',
                'parent',
            ),
        }),
    )
    

