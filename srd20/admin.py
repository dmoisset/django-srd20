from django.contrib import admin
from srd20.models import Spell, Feat, CharacterClass, Monster

class SpellAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'short_description')
    list_filter = ('school',)
    search_fields = ('name',)
    prepopulated_fields = {'altname': ('name',)}

    fieldsets = (
        (None, {
            'fields': ('name', 'altname', ('school', 'subschool'), 'descriptor', 'level', 'reference')
        }),
        ('Properties', {
            'fields': ('components', 'range', ('target', 'area', 'effect'), 'duration', 'saving_throw', 'spell_resistance')
        }),
        ('Epic requirements', {
            'fields': ('spellcraft_dc', 'to_develop'),
            'classes': ("collapse",)
        }),
        ('Description', {
            'fields': ('short_description', 'description', 'verbal_components',
            'material_components', 'arcane_material_components', 'focus',
            'arcane_focus', 'cleric_focus', 'druid_focus','xp_cost')
        }),
    )

class FeatAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)
    prepopulated_fields = {'altname': ('name',)}

    fieldsets = (
        (None, {
            'fields': ('name', 'altname', 'type', ('multiple', 'stack'), 'prerequisite', 'choice')
        }),
        ('Description', {
            'fields': ('benefit', 'normal', 'special')
        }),
        ('Source', {
            'fields': ('reference',),
        }),
    )

class MonsterAdmin(admin.ModelAdmin):
    list_display = ('name', 'alignment', 'size', 'type', 'environment', 'cr')
    list_filter = ('cr', 'type', 'size', 'alignment', 'reference')
    search_fields = ('name',)

admin.site.register(Spell, SpellAdmin)
admin.site.register(Feat, FeatAdmin)
admin.site.register(Monster, MonsterAdmin)
admin.site.register(CharacterClass)

