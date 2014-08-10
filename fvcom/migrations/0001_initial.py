# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Station'
        db.create_table(u'fvcom_station', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stations', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fvcom.StationIndex'])),
            ('file_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'fvcom', ['Station'])

        # Adding model 'Model'
        db.create_table(u'fvcom_model', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('web_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('display_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('model_type', self.gf('django.db.models.fields.CharField')(default='HINDCAST', max_length=15)),
            ('time_series', self.gf('django.db.models.fields.BooleanField')()),
            ('center_longitude', self.gf('django.db.models.fields.IntegerField')()),
            ('center_latitude', self.gf('django.db.models.fields.IntegerField')()),
            ('zoom_level', self.gf('django.db.models.fields.IntegerField')()),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fvcom.StationIndex'], blank=True)),
        ))
        db.send_create_signal(u'fvcom', ['Model'])

        # Adding model 'StationIndex'
        db.create_table(u'fvcom_stationindex', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('web_folder_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'fvcom', ['StationIndex'])


    def backwards(self, orm):
        # Deleting model 'Station'
        db.delete_table(u'fvcom_station')

        # Deleting model 'Model'
        db.delete_table(u'fvcom_model')

        # Deleting model 'StationIndex'
        db.delete_table(u'fvcom_stationindex')


    models = {
        u'fvcom.model': {
            'Meta': {'object_name': 'Model'},
            'center_latitude': ('django.db.models.fields.IntegerField', [], {}),
            'center_longitude': ('django.db.models.fields.IntegerField', [], {}),
            'display_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_type': ('django.db.models.fields.CharField', [], {'default': "'HINDCAST'", 'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fvcom.StationIndex']", 'blank': 'True'}),
            'time_series': ('django.db.models.fields.BooleanField', [], {}),
            'web_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'zoom_level': ('django.db.models.fields.IntegerField', [], {})
        },
        u'fvcom.station': {
            'Meta': {'object_name': 'Station'},
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'stations': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fvcom.StationIndex']"})
        },
        u'fvcom.stationindex': {
            'Meta': {'object_name': 'StationIndex'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'web_folder_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['fvcom']