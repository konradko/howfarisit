import unittest
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.test import TestCase
from django.conf import settings

import tools

class TestTools(TestCase):

    destination = (-0.109762, 51.522199)

    def test_calc_distance(self):
        distance = tools.calc_distance(self.destination, self.destination)
        self.assertEqual(distance, 0)

    def test_get_lon_lat(self):
        lon_lat = tools.get_lon_lat('google.com')
        self.assertTrue(isinstance(lon_lat, tuple))

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