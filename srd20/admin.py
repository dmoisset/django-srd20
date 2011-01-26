from django.contrib import admin
from srd20.models import Spell

class SpellAdmin(admin.ModelAdmin):
    pass

admin.site.register(Spell, SpellAdmin)
