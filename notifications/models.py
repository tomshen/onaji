from django.db import models
from django.core.mail import send_mail
from twilio.rest import TwilioRestClient

from subscribers.models import Subscriber
from secrets import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

class Notification(models.Model):
    notification_id = models.IntegerField(blank=True, default=0)
    title = models.CharField(max_length=64)
    content = models.TextField(blank=True)
    poster = models.CharField(blank=True, max_length=64, default='admin')
    post_date = models.DateTimeField(auto_now_add=True)
    tweet_this = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)

    def send_notification(self):
        try:
            emails = []
            phone_numbers = []
            for sub in Subscriber.objects.all():
                if sub.email:
                    emails.append(sub.email)
                if sub.phone:
                    phone_numbers.append(sub.phone)
            for email in emails:
                send_mail('Notification: ' + self.title, 
                    self.content, 'Onaji Events events@onaji.mailgun.org', [email])
            client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            for phone in phone_numbers:
                if len(phone) == 10:
                    phone = '1' + phone
                if len(phone) == 11 and phone.index('1') == 0:
                    phone = '+' + phone
                    message = client.sms.messages.create(
                        to=phone, from_='+17174849472', body=self.title)
            if self.tweet_this:
                import secrets
                import twitter
                api = twitter.Api(consumer_key=secrets.TWITTER_CONSUMER_KEY, 
                    consumer_secret=secrets.TWITTER_CONSUMER_SECRET, 
                    access_token_key=secrets.TWITTER_ACCESS_TOKEN_KEY, 
                    access_token_secret=secrets.TWITTER_ACCESS_TOKEN_SECRET)
                update = self.title
                if len(self.content) > 138 - len(self.title):
                    update += ': ' + self.content[:138 - len(self.title) - 3] + '...'
                else:
                    update += ': ' + self.content
                api.PostUpdate(update)
            self.sent = True
            self.save()
            print 'notification sent: ' + self.title + ' on ' + self.post_date.isoformat()
        except:
            print 'notification failed: ' + self.title + ' on ' + self.post_date.isoformat()

    def __unicode__(self):
        uni_rep = unicode(self.title)
        if self.content:
            uni_rep += ': ' + unicode(self.content)
        return uni_rep + '. Posted at ' + unicode(self.post_date)

    class Meta:
        ordering = ('post_date',)