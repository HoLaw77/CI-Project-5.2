from django.test import TestCase
from .models import Order, OrderDetail


class Test_Checkout_Model(TestCase):

    def setUp(self):
        Order.objects.create(

            full_name = "test", 

            country = "USA",

            email = "test@test.com", 

            phone_number = "1234567", 

            address1 = "Test street", 

            address2 = "Pass",
        
            postcode = "CF98 7up", 

            order_total = 10, 

            delivery_cost = 5, 

            overall_total = 15, 
        )

        OrderDetail.objects.create(
    

            item_total = 10


        )

    def test_order_generate_total(self):
        order_detail = OrderDetail.objects.get(item_total=10)
        self.assertEqual(order_detail.order.order_total, 10)
        self.assertEqual(order_detail.order.delivery_cost, 5)