from django.test import TestCase
from .models import Order, OrderDetail
from .forms import ConfirmOrder

class ConfirmOrderForm(TestCase):

    def test_full_name_is_required(self):
        """test full_name is required""" 
        form = ConfirmOrder({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')
    
    def test_country_is_required(self):
        """test country is required""" 
        form = ConfirmOrder({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0], 'This field is required.')
    
    def test_email_is_required(self):
        """test email is required"""
        form = ConfirmOrder({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_address1_is_required(self):
        """test address1 is required"""
        form = ConfirmOrder({'address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('address1', form.errors.keys())
        self.assertEqual(form.errors['address1'][0], 'This field is required.')

    def test_address2_is_required(self):
        """test address2 is required"""
        form = ConfirmOrder({'address2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('address2', form.errors.keys())
        self.assertEqual(form.errors['address2'][0], 'This field is required.')

    def test_postcode_is_required(self):
        """test postcode is required"""
        form = ConfirmOrder({'postcode': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('postcode', form.errors.keys())
        self.assertEqual(form.errors['postcode'][0], 'This field is required.')

    def test_form_init(self):
        """test Confirm Order form init by creating an instance"""
        form = ConfirmOrder()
        self.assertIsInstance(form, ConfirmOrder)

    
