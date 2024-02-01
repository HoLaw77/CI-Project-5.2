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

    