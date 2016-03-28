# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gear'
        db.create_table(u'price_history_gear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'price_history', ['Gear'])

        # Adding model 'Url'
        db.create_table(u'price_history_url', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('xpath', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('store_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('gear', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['price_history.Gear'])),
        ))
        db.send_create_signal(u'price_history', ['Url'])

        # Adding model 'PriceHistory'
        db.create_table(u'price_history_pricehistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('store_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('gear', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['price_history.Gear'])),
        ))
        db.send_create_signal(u'price_history', ['PriceHistory'])


    def backwards(self, orm):
        # Deleting model 'Gear'
        db.delete_table(u'price_history_gear')

        # Deleting model 'Url'
        db.delete_table(u'price_history_url')

        # Deleting model 'PriceHistory'
        db.delete_table(u'price_history_pricehistory')


    models = {
        u'price_history.gear': {
            'Meta': {'object_name': 'Gear'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'price_history.pricehistory': {
            'Meta': {'object_name': 'PriceHistory'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gear': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['price_history.Gear']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'store_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'price_history.url': {
            'Meta': {'object_name': 'Url'},
            'gear': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['price_history.Gear']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'store_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'xpath': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['price_history']