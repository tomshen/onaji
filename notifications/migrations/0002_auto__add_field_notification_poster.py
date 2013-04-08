# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Notification.poster'
        db.add_column(u'notifications_notification', 'poster',
                      self.gf('django.db.models.fields.CharField')(default='admin', max_length=64, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Notification.poster'
        db.delete_column(u'notifications_notification', 'poster')


    models = {
        u'notifications.notification': {
            'Meta': {'ordering': "('post_date',)", 'object_name': 'Notification'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notification_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {}),
            'poster': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '64', 'blank': 'True'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'tweet_this': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['notifications']