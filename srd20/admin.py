from django.contrib import admin
from srd20.models import Spell

class SpellAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'short_description')
    list_filter = ('school',)
    search_fields = ('name',)

admin.site.register(Spell, SpellAdmin)
