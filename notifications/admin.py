from .models import Notification
from django.contrib import admin

class NotificationAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'poster', 'tweet_this')

admin.site.register(Notification, NotificationAdmin)