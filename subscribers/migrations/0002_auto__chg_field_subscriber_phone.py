# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Subscriber.phone'
        db.alter_column(u'subscribers_subscriber', 'phone', self.gf('django.db.models.fields.CharField')(max_length=12))

    def backwards(self, orm):

        # Changing field 'Subscriber.phone'
        db.alter_column(u'subscribers_subscriber', 'phone', self.gf('django.db.models.fields.CharField')(max_length=10))

    models = {
        u'subscribers.subscriber': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Subscriber'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'})
        }
    }

    complete_apps = ['subscribers']