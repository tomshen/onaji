# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Question.poster'
        db.add_column(u'qa_question', 'poster',
                      self.gf('django.db.models.fields.CharField')(default='Anonymous', max_length=64, blank=True),
                      keep_default=False)

        # Adding field 'Question.answerer'
        db.add_column(u'qa_question', 'answerer',
                      self.gf('django.db.models.fields.CharField')(default='admin', max_length=64, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Question.poster'
        db.delete_column(u'qa_question', 'poster')

        # Deleting field 'Question.answerer'
        db.delete_column(u'qa_question', 'answerer')


    models = {
        u'qa.question': {
            'Meta': {'ordering': "('post_date',)", 'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'answered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'answerer': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '64', 'blank': 'True'}),
            'asker_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'poster': ('django.db.models.fields.CharField', [], {'default': "'Anonymous'", 'max_length': '64', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['qa']