from django.conf.urls import patterns, include, url

urlpatterns = patterns('schedule.views',
    url(r'^$', 'default'),
    url(r'^all/', 'all_events'),
    url(r'^new/', 'new_event'),
    url(r'^update/(?P<event_id>\d+)/', 'update_event'),
)