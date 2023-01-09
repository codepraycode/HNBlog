from django.utils.translation import gettext_lazy as _

# Register your base models here.

class BaseItemAdmin():
    list_display = (
        'author',
        'item_type',
    )

    search_fields = (
        'author',
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
                'dead'
                '_type',
                'time',
            ),
        }),
    )
    
    
    def author(self, obj):
        return obj.by or "Annonymous"
    
    def item_type(self, obj):
        return obj._type
