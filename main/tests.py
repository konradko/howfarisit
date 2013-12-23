import unittest
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.test import TestCase
from django.conf import settings

from main.models import Distance

class TestModel(TestCase):

    def test_distance_creation(self):
        distance = Distance(user_ip='127.0.0.1', distance=1)
        self.assertTrue(isinstance(distance, Distance))
        self.assertEqual(distance.__unicode__(), distance.distance)

class TestViews(TestCase):

    def test_view_distance(self):
        url = reverse("main.views.view_distance")
        response = Client().get(url)
        # Assuming that tests are run on locally and
        # tools.py/get_lon_lat uses different host as user address
        if settings.DEBUG:
            self.assertEqual(response.status_code, 200)
            self.assertIn('km', response.content)
        else:
            self.assertEqual(response.status_code, 500)
            self.assertIn("Sorry", response.content)

    def test_api_view(self):
        url = reverse("main.views.api_view")
        response = Client().get(url)
        # Assuming that tests are run on locally and
        # tools.py/get_lon_lat uses different host as user address
        if settings.DEBUG:
            self.assertEqual(response.status_code, 200)
            self.assertIn('Distance', response.content)
        else:
            self.assertEqual(response.status_code, 500)
            self.assertIn("Error", response.content)

if __name__ == '__main__':
    unittest.main()