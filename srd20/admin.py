from django.contrib import admin
from srd20.models import Spell
from srd20.models import Source
from srd20.models import FeatType
from srd20.models import Feat

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

class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'initials')
    search_fields = ('name', 'initials')
    prepopulated_fields = {'altname': ('name',)}


class FeatTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'altname': ('name',)}



class FeatAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)
    prepopulated_fields = {'altname': ('name',)}

    fieldsets = (
        (None, {
            'fields': ('name', 'altname', 'type')
        }),
        ('Prerequisites', {
            'fields': ('prerequisite_feats', 'prerequisite_description')
        }),
        ('Description', {
            'fields': ('short_description', 'benefit', 'normal', 'special')
        }),
        ('Source', {
            'fields': (('source', 'source_page'),),
        }),
    )


admin.site.register(Spell, SpellAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(FeatType, FeatTypeAdmin)
admin.site.register(Feat, FeatAdmin)
