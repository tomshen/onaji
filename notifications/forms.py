from django.forms import ModelForm

from .models import Notification

class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        exclude = ('notification_id', 'sent')