from django.conf.urls import patterns, include, url

urlpatterns = patterns('qa.views',
    url(r'^$', 'default'),
    url(r'^all/', 'all_questions'),
    url(r'^answered/', 'all_answered_questions'),
    url(r'^new/', 'new_question'),
    url(r'^update/(?P<question_id>\d+)/', 'update_question'),
)