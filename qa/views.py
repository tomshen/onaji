import json

from django.core import serializers

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render
from django.forms.models import model_to_dict

from .models import Question
from .forms import QuestionForm

def default(request):
    return HttpResponse('/all - GET: all questions' 
        + ' /new - POST: new question'
        + ' /update/<question_id> - POST: update questions')

def all_questions(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            raw_data = serializers.serialize('python', Question.objects.all().order_by('post_date'))
            # now extract the inner `fields` dicts
            actual_data = []
            for d in raw_data:
                d['fields']['question_id'] = d['pk']
                actual_data.append(d['fields'])
            for d in actual_data:
                d['post_date'] = str(d['post_date'])
            # and now dump to JSON
            clean_data = json.dumps(actual_data)
            return HttpResponse(clean_data, content_type='application/json')
        else:
            return HttpResponse('HTTP request type ' + request.method + ' not supported.')
    else:
        return HttpResponseForbidden('Not authorized for this view.')

def all_answered_questions(request):
    if request.method == 'GET':
        raw_data = serializers.serialize('python', Question.objects.all().order_by('post_date'))
        # now extract the inner `fields` dicts
        actual_data = []
        for d in raw_data:
            d['fields']['question_id'] = d['pk']
            if d['fields']['answered']:
                actual_data.append(d['fields'])
        for d in actual_data:
            d.pop('asker_email')
            d.pop('answered')
            d['post_date'] = str(d['post_date'])
        # and now dump to JSON
        clean_data = json.dumps(actual_data)
        return HttpResponse(clean_data, content_type='application/json')
    else:
        return HttpResponse('HTTP request type ' + request.method + ' not supported.')

def new_question(request):
    if request.method == 'GET':
        form = QuestionForm(request.GET)
        if 'answered' not in form and form.is_valid():
            form.save()
            return HttpResponse('Question saved.')
        else:
            return HttpResponseBadRequest('Invalid question format.')
    else:
        return HttpResponseBadRequest('HTTP request type ' + request.method + ' not supported.')

def update_question(request, question_id):
    if request.method == 'POST':
        new_data = {}
        for key, value in request.POST.items():
            new_data[key] = value
        Question.objects.filter(pk=question_id).update(**new_data)
        return HttpResponse('Question updated.')
    else:
        return HttpResponseBadRequest('HTTP request type ' + request.method + ' not supported.')