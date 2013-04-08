# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'qa_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('asker_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('answer', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('answered', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'qa', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'qa_question')


    models = {
        u'qa.question': {
            'Meta': {'ordering': "('post_date',)", 'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'answered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'asker_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['qa']