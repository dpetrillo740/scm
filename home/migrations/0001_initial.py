# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sku'
        db.create_table('home_sku', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('home', ['Sku'])


    def backwards(self, orm):
        # Deleting model 'Sku'
        db.delete_table('home_sku')


    models = {
        'home.sku': {
            'Meta': {'object_name': 'Sku'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['home']