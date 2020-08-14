from import_export import resources
from .models import Guest

class GuestResource(resources.ModelResource):
    class Meta:
        model = Guest