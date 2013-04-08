from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    poster = models.CharField(max_length=64, blank=True, default='Anonymous')
    post_date = models.DateTimeField(auto_now_add=True)
    asker_email = models.EmailField(blank=True)
    answer = models.TextField(blank=True)
    answered = models.BooleanField(default=False)
    answerer = models.CharField(max_length=64, blank=True, default='admin')

    def __unicode__(self):
        return self.title + ' asked on ' + unicode(self.post_date)

    class Meta:
        ordering = ('post_date',)