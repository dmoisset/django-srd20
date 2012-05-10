from django.contrib import admin
from encounter.models import Encounter, Participant

class ParticipantInline(admin.TabularInline):
    model = Participant

class EncounterAdmin(admin.ModelAdmin):
    inlines = [ParticipantInline]

admin.site.register(Encounter, EncounterAdmin)
