from django.db import models

from django.contrib.auth.models import User
from srd20.models import Feat, Spell

class FavoriteSpell(models.Model):
    user = models.ForeignKey(User)
    spell = models.ForeignKey(Spell)
    
    class Meta:
        unique_together = ('user', 'spell')

class FavoriteFeat(models.Model):
    user = models.ForeignKey(User)
    feat = models.ForeignKey(Feat)
    
    class Meta:
        unique_together = ('user', 'feat')


