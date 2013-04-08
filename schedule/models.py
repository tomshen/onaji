from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name + ' on ' + unicode(self.date)

    class Meta:
        ordering = ('date',)
