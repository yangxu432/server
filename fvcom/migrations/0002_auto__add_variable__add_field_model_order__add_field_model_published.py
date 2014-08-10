# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Variable'
        db.create_table(u'fvcom_variable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fvcom.Model'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('NCDF_variable', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'fvcom', ['Variable'])

        # Adding field 'Model.order'
        db.add_column(u'fvcom_model', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Model.published'
        db.add_column(u'fvcom_model', 'published',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Variable'
        db.delete_table(u'fvcom_variable')

        # Deleting field 'Model.order'
        db.delete_column(u'fvcom_model', 'order')

        # Deleting field 'Model.published'
        db.delete_column(u'fvcom_model', 'published')


    models = {
        u'fvcom.model': {
            'Meta': {'object_name': 'Model'},
            'center_latitude': ('django.db.models.fields.IntegerField', [], {}),
            'center_longitude': ('django.db.models.fields.IntegerField', [], {}),
            'display_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_type': ('django.db.models.fields.CharField', [], {'default': "'HINDCAST'", 'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {}),
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
        },
        u'fvcom.variable': {
            'Meta': {'object_name': 'Variable'},
            'NCDF_variable': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fvcom.Model']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['fvcom']