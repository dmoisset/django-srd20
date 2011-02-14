# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Source'
        db.create_table('srd20_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('altname', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('srd20', ['Source'])

        # Adding model 'FeatType'
        db.create_table('srd20_feattype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('altname', self.gf('django.db.models.fields.SlugField')(max_length=30, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('srd20', ['FeatType'])

        # Adding model 'Feat'
        db.create_table('srd20_feat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('altname', self.gf('django.db.models.fields.SlugField')(max_length=30, db_index=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['srd20.FeatType'])),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('prerequisite_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('benefit', self.gf('django.db.models.fields.TextField')()),
            ('normal', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('special', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['srd20.Source'], blank=True)),
            ('source_page', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('srd20', ['Feat'])

        # Adding M2M table for field prerequisite_feats on 'Feat'
        db.create_table('srd20_feat_prerequisite_feats', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_feat', models.ForeignKey(orm['srd20.feat'], null=False)),
            ('to_feat', models.ForeignKey(orm['srd20.feat'], null=False))
        ))
        db.create_unique('srd20_feat_prerequisite_feats', ['from_feat_id', 'to_feat_id'])


    def backwards(self, orm):
        
        # Deleting model 'Source'
        db.delete_table('srd20_source')

        # Deleting model 'FeatType'
        db.delete_table('srd20_feattype')

        # Deleting model 'Feat'
        db.delete_table('srd20_feat')

        # Removing M2M table for field prerequisite_feats on 'Feat'
        db.delete_table('srd20_feat_prerequisite_feats')


    models = {
        'srd20.feat': {
            'Meta': {'object_name': 'Feat'},
            'altname': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'db_index': 'True'}),
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'normal': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'prerequisite_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'prerequisite_feats': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['srd20.Feat']", 'symmetrical': 'False', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['srd20.Source']", 'blank': 'True'}),
            'source_page': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'special': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['srd20.FeatType']"})
        },
        'srd20.feattype': {
            'Meta': {'object_name': 'FeatType'},
            'altname': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'srd20.source': {
            'Meta': {'object_name': 'Source'},
            'altname': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'srd20.spell': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Spell', 'db_table': "'spell'"},
            'altname': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'arcane_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'arcane_material_components': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'casting_time': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'cleric_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'components': ('django.db.models.fields.TextField', [], {}),
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
