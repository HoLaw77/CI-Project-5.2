from django.test import TestCase
from product.models import Product, ProductImage


class Test_Order_Views(TestCase):
    
    def setUp(self):
        """Set up data for testing"""

        Product.objects.create(
            cover = 1,
            year_of_publication = 1998,
            name = "La vie",
            publisher = "folio",
            author = "Romeo",
            number_of_pages = 4,
            isbn = "9780099302780",

        )

    