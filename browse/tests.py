from django.test import TestCase
from django.contrib.auth.models import User, Permission

class BrowseTest(TestCase):
    fixtures = ['srd.json']

    def test_get(self):
        response = self.client.get('/browse/spell/alarm/')
        # Check that we got a result
        self.assertEqual(200, response.status_code)
        # Check that the requested spellwas in the context
        self.assertEqual('alarm', response.context['spell'].altname)
    
    def test_get_complex_slug(self):
        """This test intended to check that the slug regex is OK and works with dashes and uppercase"""
        response = self.client.get('/browse/spell/summon-natures-ally-VI/')
        self.assertEqual(200, response.status_code)
        self.assertEqual('summon-natures-ally-VI', response.context['spell'].altname)

    def test_get_404(self):
        response = self.client.get('/browse/spell/does-not-exist/')
        # Check that we got a 404 result
        self.assertEqual(404, response.status_code)
    
    def test_anonymous_cant_edit(self):
        response = self.client.get('/browse/spell/alarm/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.context['editable'])

    def test_authenticated_cantedit(self):
        authenticated, _ = User.objects.get_or_create(
            username='testuser',
            password='*',
            is_staff=True
        )
        authenticated.set_password('test')
        authenticated.user_permissions.add(Permission.objects.get(codename='change_spell', content_type__app_label='srd20'))
        authenticated.save()
        self.client.login(username='testuser',password='test')
        response = self.client.get('/browse/spell/alarm/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.context['editable'])

