from django.db import models

class Subscriber(models.Model):
    name = models.CharField(blank=True, max_length=64)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True, max_length=12)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ('name',)