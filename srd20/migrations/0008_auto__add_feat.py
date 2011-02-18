# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Feat'
        db.create_table('feat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('altname', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=64, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('multiple', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('stack', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('choice', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('prerequisite', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('benefit', self.gf('django.db.models.fields.TextField')()),
            ('normal', self.gf('django.db.models.fields.TextField')()),
            ('special', self.gf('django.db.models.fields.TextField')()),
            ('full_text', self.gf('django.db.models.fields.TextField')()),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('srd20', ['Feat'])


    def backwards(self, orm):
        
        # Deleting model 'Feat'
        db.delete_table('feat')


    models = {
        'srd20.feat': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Feat', 'db_table': "'feat'"},
            'altname': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'choice': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'full_text': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiple': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'normal': ('django.db.models.fields.TextField', [], {}),
            'prerequisite': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'special': ('django.db.models.fields.TextField', [], {}),
            'stack': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'srd20.spell': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Spell', 'db_table': "'spell'"},
            'altname': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'arcane_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'arcane_material_components': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'casting_time': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'cleric_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'components': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descriptor': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'druid_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'effect': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'focus': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'material_components': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'range': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'saving_throw': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'spell_resistance': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'spellcraft_dc': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'subschool': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'to_develop': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'verbal_components': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'xp_cost': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['srd20']
