from django.test import TestCase
from django.urls import resolve

from kruk.views import MainInaczej


class HomePageTest(TestCase):
    def test_root_page_to_main_view(self):
        found_route = resolve('/')
        self.assertEqual(found_route.func.view_class, MainInaczej)
