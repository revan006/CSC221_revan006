
import unittest
from city_functions import format_city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_location = format_city_country('santiago', 'chile')
        self.assertEqual(formatted_location, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_location = format_city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_location, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()
