from django.test import TestCase
from product.models import Product, ProductImage
from checkout.models import Order, OrderDetail
from customer.models import Profile
from django.contrib.auth.models import User
from .contexts import order_contents


class Test_Order_Views(TestCase):
    
    def setUp(self):
        """Set up data for testing"""

        self.product = Product.objects.create(
            cover = 1,
            year_of_publication = 1998,
            name = "La vie",
            publisher = "folio",
            author = "Romeo",
            number_of_pages = 4,
            isbn = "9780099302780",
            price = 4,
        )

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

        self.bag =         

    def test_show_order(self):

        response = self.client.get('/order')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/order.html')

