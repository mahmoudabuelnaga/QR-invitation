from django.contrib import admin
from .models import Country, City, Event, Event_Type, Guest, Templates

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Event)
admin.site.register(Event_Type)
admin.site.register(Guest)
admin.site.register(Templates)
