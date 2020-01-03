from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User



class TestCartView(TestCase):
    
    def test_add_to_cart_page(self):
        response = self.client.get('/cart/add_to_cart/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
    
