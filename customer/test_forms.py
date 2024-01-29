from django.test import TestCase
from .forms import ProfileForm, BookInterestForm

class TestProfileForm(TestCase):

    def test_full_name_is_required(self):
        """test full_name is required""" 
        form = ProfileForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')
    
    def test_country_is_required(self):
        """test country is required""" 
        form = ProfileForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0], 'This field is required.')
    
    def test_email_is_required(self):
        """test email is required"""
        form = ProfileForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        """test phone number is required"""
        form = ProfileForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0], 'This field is required.')

class TestBookInterestForm(TestCase):

    def test_form_is_valid(self):
        """Test for all fields optional"""
        
        form = BookInterestForm({
        
            "book_name": " ",  
            "description": " ",
        
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")