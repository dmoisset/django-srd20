# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

from srd20.models import Spell

class Migration(DataMigration):

    def forwards(self, orm):
        for s in Spell.objects.exclude(wizard_focus=''):
            assert s.wizard_focus == s.sorcerer_focus
            assert s.wizard_focus == s.bard_focus
            s.arcane_focus = s.wizard_focus
            s.wizard_focus = ''
            s.sorcerer_focus = ''
            s.bard_focus = ''
            s.save()
        assert not Spell.objects.exclude(wizard_focus='')
        assert not Spell.objects.exclude(sorcerer_focus='')
        assert not Spell.objects.exclude(bard_focus='')

    def backwards(self, orm):
        pass 
        # This could copy the arcane field to wizard/sorcerer/bard _focus
        # on the scrying spells. But I can't find the reason to revert this
        # migration


    models = {
        'srd20.spell': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Spell', 'db_table': "'spell'"},
            'altname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'arcane_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'arcane_material_components': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'bard_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'casting_time': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'cleric_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'components': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descriptor': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'druid_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'effect': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'focus': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'full_text': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'material_components': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'range': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'saving_throw': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sorcerer_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'spell_resistance': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'spellcraft_dc': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'subschool': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'to_develop': ('django.db.models.fields.TextField', [], {}),
            'verbal_components': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'wizard_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'xp_cost': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['srd20']
