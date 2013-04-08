from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

from .forms import SubscriberForm

def new_user(request):
    if request.method == 'GET':
        form = SubscriberForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse('Subscriber saved.')
        else:
            print form
            return HttpResponseBadRequest('Invalid data format.')
    else:
        return HttpResponseBadRequest('HTTP request type ' + request.method + ' not supported.')