# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Notification'
        db.create_table(u'notifications_notification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('notification_id', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('tweet_this', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'notifications', ['Notification'])


    def backwards(self, orm):
        # Deleting model 'Notification'
        db.delete_table(u'notifications_notification')


    models = {
        u'notifications.notification': {
            'Meta': {'ordering': "('post_date',)", 'object_name': 'Notification'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notification_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'tweet_this': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['notifications']