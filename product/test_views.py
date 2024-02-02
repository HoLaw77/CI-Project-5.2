from django.test import TestCase
from .models import Product, ProductImage, Language, Category

class Test_Views(TestCase):

    def setUp(self):
            
        self.language = Language.objects.create(
            language = 2,
            note = " ",
            )

        self.category = Category.objects.create(
            genre = 2,
            region = 4,
            )

        self.product = Product.objects.create(
            cover = 1,
            year_of_publication = 1998,
            name = "La vie",
            publisher = "folio",
            author = "Romeo",
            number_of_pages = 4,
            isbn = "9780099302780",
            )
        

    def test_book_detail_view(self):
        """Test book_detail can render the correct book"""
        book = Product.objects.create(product= self.product)
        book.save()
        response = self.client.get(f'/book_detail/{self.product}')
        self.assertEqual(book.name, "La vie")
            

        