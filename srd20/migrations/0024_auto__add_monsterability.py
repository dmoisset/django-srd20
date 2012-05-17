# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MonsterAbility'
        db.create_table('srd20_monsterability', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('monster', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['srd20.Monster'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('srd20', ['MonsterAbility'])


    def backwards(self, orm):
        
        # Deleting model 'MonsterAbility'
        db.delete_table('srd20_monsterability')


    models = {
        'srd20.characterclass': {
            'Meta': {'ordering': "('name',)", 'object_name': 'CharacterClass', 'db_table': "'class'"},
            'alignment': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'class_skills': ('django.db.models.fields.TextField', [], {}),
            'epic_feat_base_level': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'epic_feat_interval': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'epic_feat_list': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'epic_full_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'full_text': ('django.db.models.fields.TextField', [], {}),
            'hit_die': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'proficiencies': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'req_base_attack_bonus': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'req_epic_feat': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'req_feat': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'req_languages': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'req_psionics': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'req_race': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'req_skill': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'req_special': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'req_spells': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'req_weapon_proficiency': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'skill_points': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'skill_points_ability': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'spell_list_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spell_list_2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'spell_list_3': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'spell_list_4': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'spell_list_5': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'spell_stat': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'spell_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'srd20.feat': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Feat', 'db_table': "'feat'"},
            'altname': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'choice': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiple': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'normal': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'prerequisite': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'special': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'stack': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'srd20.monster': {
            'Meta': {'ordering': "['name']", 'object_name': 'Monster'},
            'abilities': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'alignment': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'altname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'armor_class': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'aura': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'base_attack_bonus': ('django.db.models.fields.IntegerField', [], {}),
            'charisma': ('django.db.models.fields.IntegerField', [], {}),
            'class_level': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'combat_maneuver_bonus': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'combat_maneuver_defense': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'constitution': ('django.db.models.fields.IntegerField', [], {}),
            'cr': ('django.db.models.fields.IntegerField', [], {}),
            'damage_reduction_amount': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'damage_reduction_condition': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'defensive_abilities': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dexterity': ('django.db.models.fields.IntegerField', [], {}),
            'environment': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'feats': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'flavor_text': ('django.db.models.fields.TextField', [], {}),
            'fortitude_save': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'gear': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'hit_points': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'immunities': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'initiative': ('django.db.models.fields.IntegerField', [], {}),
            'intelligence': ('django.db.models.fields.IntegerField', [], {}),
            'languages': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'melee': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'opposition_schools': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'organization': ('django.db.models.fields.TextField', [], {}),
            'other_type': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'racial_modifiers': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'ranged': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'reach': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'reflex_save': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'resistance': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'senses': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'skills': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sorcerer_spells_known': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'space': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'special_attacks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'special_qualities': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'speed': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'spell_like_abilities': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spell_resistance': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'spells_known': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spells_prepared': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'strength': ('django.db.models.fields.IntegerField', [], {}),
            'subtypes': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'treasure': ('django.db.models.fields.TextField', [], {'max_length': '128', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'weaknesses': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'will_save': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'wisdom': ('django.db.models.fields.IntegerField', [], {}),
            'xp': ('django.db.models.fields.IntegerField', [], {})
        },
        'srd20.monsterability': {
            'Meta': {'object_name': 'MonsterAbility'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'monster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['srd20.Monster']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'srd20.spell': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Spell', 'db_table': "'spell'"},
            'altname': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'arcane_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'arcane_material_components': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'casting_time': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'cleric_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'components': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descriptor': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
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
            'saving_throw': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'spell_resistance': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'spellcraft_dc': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'subschool': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'to_develop': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'verbal_components': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'xp_cost': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['srd20']
