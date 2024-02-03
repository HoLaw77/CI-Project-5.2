from django.test import TestCase
from .models import Order, OrderDetail
from product.models import Product
from customer.models import Profile
from django.contrib.auth.models import User

class TestCheckoutModel(TestCase):

    def setUp(self):

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

        self.product = Product.objects.create(
            cover=1,
            year_of_publication=1998,
            name="La vie",
            publisher="folio",
            author="Romeo",
            number_of_pages=4,
            isbn="9780099302780",
        )

        self.order = Order.objects.create(
            profile = self.profile,
            full_name="test",
            country="USA",
            email="test@test.com",
            phone_number="1234567",
            address1="Test street",
            address2="Pass",
            postcode="CF98 7up",
            order_total=10,
            delivery_cost=5,
            overall_total=15,
        )

        self.order_detail = OrderDetail.objects.create(
            order=self.order,
            product=self.product,
            item_total=10,
            quantity=1,
        )

    def test_generate_order_number(self):
        """Test Order Number successfully generated"""
        order = Order.objects.get(full_name='test')
        self.assertIsNotNone(order.order_number)

    def test_order_generate_total(self):
        """Test order model successfully generate total"""
        order = Order.objects.get(full_name='test')
        self.assertEqual(self.order_detail.order.order_total, 0)
        self.assertEqual(self.order_detail.order.delivery_cost, 0)

    def test_save(self):
        order = Order.objects.get(full_name='test')
        order.save()
        self.assertIsNotNone(order.order_number)

    