from django.test import TestCase, Client
from .models import Item


class MainViewTest(TestCase):
    def setUp(self):
        self.item = Item(
            name='Pufferfish',
            season='Summer',
            favorable_weather='Sun',
            price=200,
            description='The Pufferfish is a fish that can be caught in the ocean at The Beach or on the Beach Farm '
                        'on sunny summer days between 12pm and 4pm, or on Ginger Island during any season on Island '
                        'West (ocean), South, Southeast, and in the Pirate Cove. It can also randomly be found in '
                        'Garbage Cans during Summer, or at the Traveling Cart for 600–1,000g.',
            amount=1
        )

    def test_show_main_view(self):
        client = Client()
        response = client.get('/main/')  # Replace with the URL of your view
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, 'Stardew Valley\'s Item Tracker')  # Check for expected content

    def test_calculate_total_method(self):
        # Test that the calculate_total method returns the correct result
        expected_total = self.item.price * self.item.amount
        self.assertEqual(self.item.calculate_total(), expected_total)

    def test_product_str_method(self):
        # Test the __str__ method of the Product model
        self.assertEqual(str(self.item), 'Pufferfish')
