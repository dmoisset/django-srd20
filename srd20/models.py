from django.db import models

# Create your models here.

class Spell(models.Model):
    name = models.CharField(max_length=64)
    altname = models.CharField(max_length=64)
    school = models.CharField(max_length=32) # Probably a FK to a list
    subschool = models.CharField(max_length=32) # probably a FK to a list
    descriptor = models.CharField(max_length=64) # A Many to Many to a table. probably with an attribute (may have all of the descriptors or any of them)
    spellcraft_dc = models.CharField(max_length=64) # This should be a nullabel int, possibly with a flag for see text notes
    level = models.CharField(max_length=128) # This should be a many-to-many to class level
    components = models.TextField() # This should be a set of flags: V, S, M, F, DF, XP, ... possibly from the nullability of other fields
    casting_time = models.CharField(max_length=32) # amount + unit, sometimes with notes
    range = models.CharField(max_length=64) # Maybe normalized, but more complex
    target = models.CharField(max_length=256)
    area = models.CharField(max_length=256)
    effect = models.CharField(max_length=256)
    duration = models.CharField(max_length=128)
    saving_throw = models.CharField(max_length=128) # may be normalized, not sure 
    spell_resistance = models.CharField(max_length=64) # may be normalized, not sure 
    short_description = models.CharField(max_length=128)
    to_develop = models.TextField()
    material_components = models.TextField()
    arcane_material_components = models.CharField(max_length=256)
    focus = models.TextField()
    description = models.TextField()
    xp_cost = models.TextField()
    arcane_focus = models.CharField(max_length=256)
    wizard_focus = models.CharField(max_length=256) # Only used in scrying spells. probably could be removed
    verbal_components = models.CharField(max_length=256) # only used in 1 spell. Possibly should meld into description
    sorcerer_focus = models.CharField(max_length=256) # Overlaps with wizard_focus. remove!
    bard_focus = models.CharField(max_length=256) # Overlaps with wizard_focus. remove!
    cleric_focus = models.CharField(max_length=256)
    druid_focus = models.CharField(max_length=256)
    full_text = models.TextField()
    reference = models.CharField(max_length=30) # Should be a FK

    @models.permalink
    def get_absolute_url(self):
        return ('spell_detail', [], {'id': self.id})

    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'spell'
        ordering = ('name',)

