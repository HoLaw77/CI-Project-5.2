from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, BookInterest

class TestCustomerModel(TestCase):
        
    def setUp(self):
        """Set up data for testing"""
        
        # Create a new User instance
        self.user_instance = User.objects.create(username="hibye", password="whatEver!")

        # Check if a profile already exists for the user
        try:
            self.profile = Profile.objects.get(user=self.user_instance)
        
        except Profile.DoesNotExist:
            
            # If no profile exists, create a new one
            
            self.profile = Profile.objects.create(
                user=self.user_instance,
                full_name="test",
                country="BR",
                email="test@test.com",
                phone_number="1234567",
                address1="test street",
                address2="highway park",
                postcode="CH768PM"
            )

        # Create a new BookInterest instance associated with the Profile
        self.book_interest_instance = BookInterest.objects.create(
            profile=self.profile,
            book_name="Romeo and Juliet",
            description="It is romantic",
        )

    def test_profile_string_method(self):
        """Test string method return username"""
        username = self.user_instance.username
        self.assertEqual(username, "hibye")

    def test_book_interest_model_return_book_name(self):
        """Test string method return book name"""
        book_name = self.book_interest_instance.book_name
        self.assertEqual(book_name, "Romeo and Juliet")
