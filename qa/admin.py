from .models import Question
from django.contrib import admin

class QuestionAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'poster', 'answered', 'answer', 'asker_email', 'answerer')

admin.site.register(Question, QuestionAdmin)