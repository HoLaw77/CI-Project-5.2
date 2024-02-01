from django.test import TestCase
from .models import Product, ProductImage, Language, Category

class TestModels(TestCase):

    def setUp(self):
        """Set up data for testing"""
        Language.objects.create(
            language = 2,
            note = " ",
        )

        Category.objects.create(
            genre = 2,
            region = 4,
        )

        Product.objects.create(
            cover = 1,
            year_of_publication = 1998,
            name = "La vie",
            publisher = "folio",
            author = "Romeo",
            number_of_pages = 4,
            isbn = "9780099302780",

        )

    def test_language_choice_model(self):
        """Test Language choice being saved in model"""
        language = Language.objects.get(language=2)
        self.assertEqual(language.get_language_display(), 'French')
    
    def test_language_model_save(self):
        language = Language.objects.create(language=2, note="Note")
        language.save()
        saved_language = Language.objects.get(id=language.id) 
        self.assertEqual(saved_language.get_language_display(), "French")

    def test_category_genre_choice_model(self):
        """Test Genre choice being saved in model"""
        genre = Category.objects.get(genre=2)
        self.assertEqual(genre.get_genre_display(), 'Thriller fiction')

    def test_category__region_model(self):
        """Test Region choice being saved in model"""
        region = Category.objects.get(region=4)
        self.assertEqual(region.get_region_display(), 'France')

    def test_product_cover_choice(self):
        """Test cover choice of Product being saved in model"""
        cover = Product.objects.get(cover=1)
        self.assertEqual(cover.get_cover_display(), 'Hardback')

    def test_product_model_save(self):
        """Test product info are saved"""
        book = Product.objects.create(
            cover = 1,
            year_of_publication = 1998,
            name = "La vie",
            publisher = "folio",
            author = "Romeo",
            number_of_pages = 4,
            isbn = "9780099302780",)
        book.save()
        saved_book = Product.objects.get(id=book.id) 
        self.assertEqual(saved_book.name, "La vie")
        self.assertEqual(saved_book.publisher, "folio")
        self.assertEqual(saved_book.author, "Romeo")
        self.assertEqual(saved_book.number_of_pages, 4)
        self.assertEqual(saved_book.isbn, "9780099302780")