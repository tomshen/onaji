import json
import copy

from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.shortcuts import render
import iso8601

from .models import Event
from .forms import EventForm

def default(request):
    return HttpResponse('/all - GET: all events' 
        + ' /new - POST: new event'
        + ' /update/<event_id> - POST: update events')

def all_events(request):
    if request.method == 'GET':
        raw_data = serializers.serialize('python', Event.objects.all().order_by('date'))
        # now extract the inner `fields` dicts
        actual_data = []
        for d in raw_data:
            d['fields']['event_id'] = d['pk']
            actual_data.append(d['fields'])
        for d in actual_data:
            d['date'] = str(d['date'])
        # and now dump to JSON
        clean_data = json.dumps(actual_data)
        return HttpResponse(clean_data, content_type='application/json')
    else:
        return HttpResponse('HTTP request type ' + request.method + ' not supported.')

def new_event(request):
    if request.method == 'POST':
        raw_data = copy.deepcopy(request.POST)
        raw_data['date'] = iso8601.parse_date(raw_data['date'])
        form = EventForm(raw_data)
        if form.is_valid():
            form.save()
            return HttpResponse('Event saved.')
        else:
            return HttpResponseBadRequest('Invalid event format.')
    else:
        return HttpResponseBadRequest('HTTP request type ' + request.method + ' not supported.')

def update_event(request, event_id):
    if request.method == 'POST':
        new_data = {}
        for key, value in request.POST.items():
            new_data[key] = value
        Event.objects.filter(pk=question_id).update(**new_data)
        return HttpResponse('Event updated.')
    else:
        return HttpResponseBadRequest('HTTP request type ' + request.method + ' not supported.')
