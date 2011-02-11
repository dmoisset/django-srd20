from django.test import TestCase
from .models import Spell

class SpellModelTest(TestCase):
    fixtures = ['srd.json']

    def test_absolute_url(self):
        """Checks that get_absolute_url produces an URL that works"""
        spell = Spell.objects.get(id=1)
        url = spell.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_absolute_url_unique(self):
        """Checks that get_absolute_url returns different URLs for different objects"""
        spell1 = Spell.objects.get(id=1)
        spell2 = Spell.objects.get(id=2)
        url1 = spell1.get_absolute_url()
        url2 = spell2.get_absolute_url()
        self.assertNotEqual(url1, url2)

    def test_unicode_unique(self):
        """Checks that __unicode__ returns different values for different objects"""
        spell1 = Spell.objects.get(id=1)
        spell2 = Spell.objects.get(id=2)
        u1 = unicode(spell1)
        u2 = unicode(spell2)
        self.assertNotEqual(u1, u2)


