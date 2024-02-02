from django.test import TestCase

class TestHomeViews(TestCase):

    def test_home_page_view(self):
        """Test view return render to home page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

