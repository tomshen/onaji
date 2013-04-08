from .models import Subscriber
from django.contrib import admin

class SubscriberAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'phone')

admin.site.register(Subscriber, SubscriberAdmin)