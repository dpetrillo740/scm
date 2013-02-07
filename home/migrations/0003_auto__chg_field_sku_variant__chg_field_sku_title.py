# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Sku.variant'
        db.alter_column('home_sku', 'variant', self.gf('django.db.models.fields.CharField')(max_length=90, null=True))

        # Changing field 'Sku.title'
        db.alter_column('home_sku', 'title', self.gf('django.db.models.fields.CharField')(max_length=90, null=True))

    def backwards(self, orm):

        # Changing field 'Sku.variant'
        db.alter_column('home_sku', 'variant', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Sku.title'
        db.alter_column('home_sku', 'title', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

    models = {
        'home.sku': {
            'Meta': {'object_name': 'Sku'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '90', 'null': 'True'}),
            'variant': ('django.db.models.fields.CharField', [], {'max_length': '90', 'null': 'True'})
        }
    }

    complete_apps = ['home']