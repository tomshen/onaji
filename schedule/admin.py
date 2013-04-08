from .models import Event
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'date', 'description', 'location')

admin.site.register(Event, EventAdmin)