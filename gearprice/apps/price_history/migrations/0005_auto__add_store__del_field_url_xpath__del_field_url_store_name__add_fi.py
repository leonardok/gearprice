# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Store'
        db.create_table(u'price_history_store', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('xpath', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'price_history', ['Store'])

        # Deleting field 'Url.xpath'
        db.delete_column(u'price_history_url', 'xpath')

        # Deleting field 'Url.store_name'
        db.delete_column(u'price_history_url', 'store_name')

        # Adding field 'Url.store'
        db.add_column(u'price_history_url', 'store',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['price_history.Store'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Store'
        db.delete_table(u'price_history_store')

        # Adding field 'Url.xpath'
        db.add_column(u'price_history_url', 'xpath',
                      self.gf('django.db.models.fields.CharField')(default='dummy_xpath', max_length=500),
                      keep_default=False)

        # Adding field 'Url.store_name'
        db.add_column(u'price_history_url', 'store_name',
                      self.gf('django.db.models.fields.CharField')(default='dummy_name', max_length=100),
                      keep_default=False)

        # Deleting field 'Url.store'
        db.delete_column(u'price_history_url', 'store_id')


    models = {
        u'price_history.brand': {
            'Meta': {'object_name': 'Brand'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'price_history.gear': {
            'Meta': {'object_name': 'Gear'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['price_history.Brand']", 'null': 'True'}),
            'gear_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['price_history.GearType']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'price_history.geartype': {
            'Meta': {'object_name': 'GearType'},
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
        u'price_history.store': {
            'Meta': {'object_name': 'Store'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'xpath': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'price_history.url': {
            'Meta': {'object_name': 'Url'},
            'gear': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['price_history.Gear']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['price_history.Store']", 'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['price_history']