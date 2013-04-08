from django.conf.urls import patterns, include, url

urlpatterns = patterns('notifications.views',
    url(r'^$', 'default'),
    url(r'^all/', 'all_notifications'),
    url(r'^new/', 'new_notification'),
)