from django.db import models

class Encounter(models.Model):
    name = models.CharField(max_length=255)
    current_round = models.PositiveIntegerField(default=0)
    current_initiative = models.IntegerField(default=999)
    notes = models.TextField(blank=True)
    # participants = reverse from Participant.encounter
    #treasure = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
    
    def current_actors(self):
        """The list of actors in the current initiative"""
        return self.participants.filter(initiative=self.current_initiative)
    
class Participant(models.Model):
    encounter = models.ForeignKey(Encounter, related_name='participants')
    label = models.CharField(max_length=32)
    current_hp = models.IntegerField(blank=True, null=True)
    initiative = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)
    #stats = ...
    #conditions = [(Condition, final_round, final_initiative)]
    
#class ParticipantCondition
#    who = Participant
#    what = Condition
#    until_round = int
#    until_initiative = int
#    notes = ...
    
    
#class Condition:
#    affects_defense = True
#    affects_offense = True
#    can_act = True

