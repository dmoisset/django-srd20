# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Spell'
        db.create_table('spell', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('altname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('subschool', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('descriptor', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('spellcraft_dc', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('components', self.gf('django.db.models.fields.TextField')()),
            ('casting_time', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('range', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('target', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('effect', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('saving_throw', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('spell_resistance', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('to_develop', self.gf('django.db.models.fields.TextField')()),
            ('material_components', self.gf('django.db.models.fields.TextField')()),
            ('arcane_material_components', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('focus', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('xp_cost', self.gf('django.db.models.fields.TextField')()),
            ('arcane_focus', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('wizard_focus', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('verbal_components', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sorcerer_focus', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('bard_focus', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('cleric_focus', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('druid_focus', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('full_text', self.gf('django.db.models.fields.TextField')()),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('srd20', ['Spell'])


    def backwards(self, orm):
        
        # Deleting model 'Spell'
        db.delete_table('spell')


    models = {
        'srd20.spell': {
            'Meta': {'object_name': 'Spell', 'db_table': "'spell'"},
            'altname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'arcane_focus': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'arcane_material_components': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'bard_focus': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'casting_time': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'cleric_focus': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'components': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'descriptor': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'druid_focus': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'effect': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'focus': ('django.db.models.fields.TextField', [], {}),
            'full_text': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'material_components': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'range': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'saving_throw': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sorcerer_focus': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'spell_resistance': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'spellcraft_dc': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'subschool': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'to_develop': ('django.db.models.fields.TextField', [], {}),
            'verbal_components': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'wizard_focus': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'xp_cost': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['srd20']
