from django.db import models

class Spell(models.Model):
    name = models.CharField(max_length=64,
        help_text='Complete spell name. Use proper capitalization, and put the '
                  'base name of the spell at the front, i.e. "Heal, Mass" '
                  'instead of "Mass Heal".')
    altname = models.SlugField(max_length=64,
        help_text='URL version of the name; use only alphanumeric char, dashes '
                  'and keep the text in lowercase except for roman numerals.')
    school = models.CharField(max_length=32,
        help_text='School of magic, for example "Illusion"') # Probably a FK to a list
    subschool = models.CharField(max_length=32, blank=True,
        help_text='Subschool of the magic school, if any. Example: "Figment"') # probably a FK to a list
    descriptor = models.CharField(max_length=64, blank=True,
        help_text='Descriptor list (comma separated). Example "Fire, Chaos"') # A Many to Many to a table. probably with an attribute (may have all of the descriptors or any of them)
    spellcraft_dc = models.CharField(max_length=64, blank=True,
        verbose_name='Spellcraft DC',
        help_text='DC to cast (epic spells)') # This should be a nullable int, possibly with a flag for see text notes
    level = models.CharField(max_length=128, blank=True,
        help_text='Comma separated list of Class lvl. Example: "Bard 3, Sor/Wiz 4"') # This should be a many-to-many to class level
    components = models.CharField(max_length=64,
        help_text='Comma separated list,as shown in spell. Example: "V, S, M/DF, XP"') # This should be a set of flags: V, S, M, F, DF, XP, ... possibly from the nullability of other fields
    casting_time = models.CharField(max_length=32) # amount + unit, sometimes with notes
    range = models.CharField(max_length=64) # Maybe normalized, but more complex
    target = models.CharField(max_length=256, blank=True)
    area = models.CharField(max_length=256, blank=True)
    effect = models.CharField(max_length=256, blank=True)
    duration = models.CharField(max_length=128)
    saving_throw = models.CharField(max_length=128) # may be normalized, not sure 
    spell_resistance = models.CharField(max_length=64) # may be normalized, not sure 
    short_description = models.CharField(max_length=128,
        help_text='Short description shown in spell lists')
    to_develop = models.TextField(blank=True,
        help_text='Cost to develop epic spell')
    material_components = models.TextField(blank=True)
    arcane_material_components = models.CharField(max_length=256, blank=True)
    focus = models.TextField(blank=True)
    description = models.TextField(blank=True)
    xp_cost = models.TextField(blank=True)
    arcane_focus = models.CharField(max_length=256, blank=True)
    verbal_components = models.CharField(max_length=256, blank=True) # only used in 1 spell. Possibly should meld into description
    cleric_focus = models.CharField(max_length=256, blank=True)
    druid_focus = models.CharField(max_length=256, blank=True)
    reference = models.CharField(max_length=30,
        help_text='Book containing the spell and pag. Example: "SpC 31"') # Should be a FK

    @models.permalink
    def get_absolute_url(self):
        return ('spell_detail', [], {'slug': self.altname})

    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'spell'
        ordering = ('name',)

class Feat(models.Model):
    name = models.CharField(max_length=64)
    altname = models.SlugField(max_length=64, blank=True, null=True)
    type = models.CharField(max_length=32) # Many to many
    multiple = models.CharField(max_length=4) # Should be updated to a booleanfield
    stack = models.CharField(max_length=4) # Should be updated to a booleanfield
    choice = models.CharField(max_length=256)
    prerequisite = models.CharField(max_length=512)
    benefit = models.TextField()
    normal = models.TextField()
    special = models.TextField()
    full_text = models.TextField()
    reference = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'feat'
        ordering = ('name',)

