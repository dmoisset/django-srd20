# encoding: utf-8
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
    subschool = models.CharField(max_length=128, blank=True,
        help_text='Subschool of the magic school, if any. Example: "Figment"') # probably a FK to a list
    descriptor = models.CharField(max_length=256, blank=True,
        help_text='Descriptor list (comma separated). Example "Fire, Chaos"') # A Many to Many to a table. probably with an attribute (may have all of the descriptors or any of them)
    spellcraft_dc = models.CharField(max_length=64, blank=True,
        verbose_name='Spellcraft DC',
        help_text='DC to cast (epic spells)') # This should be a nullable int, possibly with a flag for see text notes
    level = models.CharField(max_length=128, blank=True,
        help_text='Comma separated list of Class lvl. Example: "Bard 3, Sor/Wiz 4"') # This should be a many-to-many to class level
    components = models.CharField(max_length=256,
        help_text='Comma separated list,as shown in spell. Example: "V, S, M/DF, XP"') # This should be a set of flags: V, S, M, F, DF, XP, ... possibly from the nullability of other fields
    casting_time = models.CharField(max_length=64) # amount + unit, sometimes with notes
    range = models.CharField(max_length=64) # Maybe normalized, but more complex
    target = models.CharField(max_length=256, blank=True)
    area = models.CharField(max_length=256, blank=True)
    effect = models.CharField(max_length=256, blank=True)
    duration = models.CharField(max_length=128)
    saving_throw = models.CharField(max_length=256) # may be normalized, not sure 
    spell_resistance = models.CharField(max_length=64) # may be normalized, not sure 
    short_description = models.CharField(max_length=256,
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
    altname = models.SlugField(max_length=64)
    type = models.CharField(max_length=32) # Should be a Many to many, perhaps with an epic flag
    multiple = models.BooleanField()
    stack = models.BooleanField()
    choice = models.CharField(max_length=256, blank=True)
    prerequisite = models.CharField(max_length=1024, blank=True)
    benefit = models.TextField()
    description = models.TextField(blank=True)
    normal = models.TextField(blank=True)
    special = models.TextField(blank=True)
    reference = models.CharField(max_length=32)
    
    def short_description(self):
        return self.description
    
    @models.permalink
    def get_absolute_url(self):
        return ('feat_detail', [], {'slug': self.altname})

    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'feat'
        ordering = ('name',)


class CharacterClass(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32) # should be flags: base/prestige, npc or not, epic or not, psionic or not
    alignment = models.CharField(max_length=128) # Should be M2M to alignemnt table
    hit_die = models.CharField(max_length=4) # Should be integer field
    class_skills = models.TextField() # Maybe a M2M to skill, but there are some special cases
    skill_points = models.CharField(max_length=1) # Should be integer field
    skill_points_ability = models.CharField(max_length=3) # Always intelligence! remove?
    spell_stat = models.CharField(max_length=4, blank=True) # ChoiceField, with empty choice
    proficiencies = models.TextField(blank=True)
    spell_type = models.CharField(max_length=16) # m2m to Arcane, Divine, Psionic
    epic_feat_base_level = models.CharField(max_length=4) # Nullable integer field
    epic_feat_interval = models.CharField(max_length=4) # Nullable integer field
    epic_feat_list = models.TextField(blank=True)
    epic_full_text = models.TextField(blank=True)
    req_race = models.CharField(max_length=64, blank=True)
    req_weapon_proficiency = models.CharField(max_length=64, blank=True) # Only Eldritch Knight uses this field
    req_base_attack_bonus = models.CharField(max_length=4,blank=True) # Nullable integer field
    req_skill = models.CharField(max_length=128, blank=True) # May be normalized but has special cases
    req_feat = models.CharField(max_length=128, blank=True) # May be normalized but has special cases
    req_spells = models.CharField(max_length=128,blank=True)
    req_languages = models.CharField(max_length=16, blank=True) # Only Dragon Disciple uses this
    req_psionics = models.CharField(max_length=64,blank=True)
    req_epic_feat = models.CharField(max_length=64, blank=True) # Probably M2M
    req_special = models.CharField(max_length=256, blank=True)
    spell_list_1 = models.TextField(blank=True) # M2M
    spell_list_2 = models.CharField(max_length=256, blank=True) # M2M
    spell_list_3 = models.CharField(max_length=256, blank=True) # M2M
    spell_list_4 = models.CharField(max_length=256, blank=True) # M2M
    spell_list_5 = models.CharField(max_length=256, blank=True) # M2M
    full_text = models.TextField()
    reference = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'class'
        ordering = ('name',)
        verbose_name_plural = 'character classes'

class Monster(models.Model):

    SIZE_CHOICES = (
        (-4, 'Fine'),
        (-3, 'Diminutive'),
        (-2, 'Tiny'),
        (-1, 'Small'),
        ( 0, 'Medium'),
        ( 1, 'Large'),
        ( 2, 'Huge'),
        ( 3, 'Gargantuan'),
        ( 4, 'Colossal'),
    )

    TYPES = [
        'aberration', 'animal', 'construct', 'dragon', 'fey', 'humanoid',
        'magical beast', 'monstrous humanoid', 'ooze', 'outsider', 'plant',
        'undead', 'vermin'
    ]
    TYPE_CHOICES = [(t, t.capitalize()) for t in TYPES]
    CR_CHOICES = [
        (-4, u'⅛'),
        (-3, u'⅙'),
        (-2, u'¼'),
        (-1, u'⅓'),
        (0, u'½'),
    ] + [(i, str(i)) for i in range(1,31)]

    name = models.CharField(max_length=64)
    altname = models.CharField(max_length=64)
    flavor_text = models.TextField()

    # Basic information
    cr = models.IntegerField(choices=CR_CHOICES)
    xp = models.IntegerField() # This should be a function of cr
    alignment = models.CharField(max_length=4)  # May be "Any", or a specific alignment coded in the usual style
    size = models.IntegerField(choices=SIZE_CHOICES)
    type = models.CharField(choices=TYPE_CHOICES, max_length=32)
    subtypes = models.CharField(max_length=64, blank=True)
    other_type = models.CharField(max_length=64, blank=True) # Other type information (for example base creatur for inherited templates)
    class_level = models.CharField(max_length=16, blank=True)
    initiative = models.IntegerField()
    senses = models.CharField(max_length=512, blank=True)
    aura = models.CharField(max_length=256, blank=True)

    # Defense
    armor_class = models.CharField(max_length=256)
    hit_points = models.CharField(max_length=256)
     # The saves are typically integers, but sometimes mention modifiers
    fortitude_save = models.CharField(max_length=256)
    reflex_save = models.CharField(max_length=128)
    will_save = models.CharField(max_length=256)
    defensive_abilities = models.CharField(max_length=256, blank=True)
    damage_reduction_amount = models.PositiveIntegerField(default=0)
    damage_reduction_condition = models.CharField(max_length=128, blank=True)
    immunities = models.CharField(max_length=1024, blank=True)
    resistance = models.CharField(max_length=256, blank=True)
    spell_resistance = models.PositiveIntegerField(default=0)
    weaknesses = models.CharField(max_length=256, blank=True)

    # Offense
    speed = models.CharField(max_length=128, blank=True)
    melee = models.CharField(max_length=512, blank=True)
    ranged = models.CharField(max_length=256, blank=True)
    space = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    reach = models.CharField(max_length=128, blank=True) # Not a decimalfield, usually includes clarifications
    special_attacks = models.TextField(blank=True)
    spell_like_abilities = models.TextField(blank=True)
    spells_known = models.TextField(blank=True)
    sorcerer_spells_known = models.TextField(blank=True)
    spells_prepared = models.TextField(blank=True)
    opposition_schools = models.CharField(max_length=64, blank=True)
    # TODO: domains
    
    # Statistics
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    base_attack_bonus = models.IntegerField()
    combat_maneuver_bonus = models.CharField(max_length=64)
    combat_maneuver_defense = models.CharField(max_length=64)
    feats = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    racial_modifiers = models.CharField(max_length=512, blank=True)
    languages = models.TextField(blank=True)
    special_qualities = models.CharField(max_length=512, blank=True)
    gear = models.CharField(max_length=128, blank=True)

    # Ecology
    environment = models.CharField(max_length=256)
    organization = models.TextField()
    treasure = models.TextField(blank=True)

    # Other
    abilities = models.TextField(blank=True)
    description = models.TextField(blank=True)
    reference = models.CharField(max_length=64)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('monster_detail', [], {'slug': self.altname})
    
    def short_description(self):
        subtypes = "(%s)" % self.subtypes if self.subtypes else ""
        cclass = ""
        result = "CR%s %s %s %s %s" % (self.get_cr_display(), self.alignment, self.get_size_display(), self.type, subtypes)
        return result

class MonsterAbility(models.Model):
    ABILITY_KINDS = (
        ('sp', 'Spell-Like'),
        ('su', 'Supernatural'),
        ('ex', 'Extraordinary'),
    )
    monster = models.ForeignKey(Monster)
    name = models.CharField(max_length=128)
    kind = models.CharField(max_length=2, choices=ABILITY_KINDS)
    description = models.TextField()

