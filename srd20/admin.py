from django.contrib import admin
from srd20.models import Spell

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

admin.site.register(Spell, SpellAdmin)
