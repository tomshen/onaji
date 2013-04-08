import string

from django.forms import ModelForm, ValidationError

from .models import Subscriber

class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber