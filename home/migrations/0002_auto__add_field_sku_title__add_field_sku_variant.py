# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sku.title'
        db.add_column('home_sku', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Adding field 'Sku.variant'
        db.add_column('home_sku', 'variant',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sku.title'
        db.delete_column('home_sku', 'title')

        # Deleting field 'Sku.variant'
        db.delete_column('home_sku', 'variant')


    models = {
        'home.sku': {
            'Meta': {'object_name': 'Sku'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'variant': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'})
        }
    }

    complete_apps = ['home']