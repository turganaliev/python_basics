import unittest
from city_functions import get_place_name

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        places_name = get_place_name('santiago', 'chilie')
        self.assertEqual(places_name, 'Santiago, Chilie')

    def test_city_country_population(self):
        places_name = get_place_name('santiago', 'chilie', 500000)
        self.assertEqual(places_name, 'Santiago, Chilie - population 500000')

unittest.main()
