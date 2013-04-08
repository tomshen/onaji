import json
import copy

from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
import iso8601

from .models import Notification
from .forms import NotificationForm

def default(request):
    return HttpResponse('/all - GET: all notifications' + '\n' + '/new - POST: new notification')

def all_notifications(request):
    if request.method == 'GET':
        raw_data = serializers.serialize('python', Notification.objects.all().order_by('-post_date'))
        # now extract the inner `fields` dicts
        actual_data = []
        for d in raw_data:
            actual_data.append(d['fields'])
            actual_data[len(actual_data) - 1].pop('notification_id')
            actual_data[len(actual_data) - 1].pop('tweet_this')
        for d in actual_data:
            d['post_date'] = str(d['post_date'])
        # and now dump to JSON
        clean_data = json.dumps(actual_data)
        return HttpResponse(clean_data, content_type='application/json')
    else:
        return HttpResponse('HTTP request type ' + request.method + ' not supported.')

def new_notification(request):
    if request.method == 'POST':
        raw_data = copy.deepcopy(request.POST)
        if 'post_date' in raw_data:
            raw_data['post_date'] = iso8601.parse_date(raw_data['post_date'])
        raw_data['notification_id'] = 0
        form = NotificationForm(raw_data)
        if form.is_valid():
            form.save()
            for note in Notification.objects.all().order_by('-post_date'):
                if note.sent:
                    break
                note.send_notification()
            return HttpResponse('Notification saved.')
        else:
            return HttpResponseBadRequest('Invalid notification format.')
    else:
        return HttpResponseBadRequest('HTTP request type ' + request.method + ' not supported.')