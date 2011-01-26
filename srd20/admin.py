from django.contrib import admin
from srd20.models import Spell

class SpellAdmin(admin.ModelAdmin):
    list_display= ('name', 'level', 'short_description')

admin.site.register(Spell, SpellAdmin)
