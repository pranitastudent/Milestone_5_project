from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# PLEASE NOTE ALL URLS TESTS WERE CODED FOR USING - Django Testing Tutorial - Testing Views #3 - The Dumbfounds.
class TestAccountsViews(TestCase):

    def test_registration_page(self):
        response = self.client.get('/accounts/register/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
