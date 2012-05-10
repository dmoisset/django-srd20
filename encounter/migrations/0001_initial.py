# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Encounter'
        db.create_table('encounter_encounter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('current_round', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('current_initiative', self.gf('django.db.models.fields.IntegerField')(default=999)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('encounter', ['Encounter'])

        # Adding model 'Participant'
        db.create_table('encounter_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encounter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='participants', to=orm['encounter.Encounter'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('current_hp', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('initiative', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('encounter', ['Participant'])


    def backwards(self, orm):
        
        # Deleting model 'Encounter'
        db.delete_table('encounter_encounter')

        # Deleting model 'Participant'
        db.delete_table('encounter_participant')


    models = {
        'encounter.encounter': {
            'Meta': {'object_name': 'Encounter'},
            'current_initiative': ('django.db.models.fields.IntegerField', [], {'default': '999'}),
            'current_round': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'encounter.participant': {
            'Meta': {'object_name': 'Participant'},
            'current_hp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encounter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'participants'", 'to': "orm['encounter.Encounter']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiative': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['encounter']
