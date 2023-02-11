from django.utils.translation import gettext_lazy as _

# Register your base models here.

class BaseItemAdmin():
    
    def author(self, obj):
        return obj.by or "Annonymous"
    
    def item_type(self, obj):
        return obj.type
    
    def comments(self, obj):
        return obj.descendants
