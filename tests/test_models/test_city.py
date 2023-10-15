#!/usr/bin/python3
"""test classs city"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.city = City()

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_to_dict(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['state_id'], city.state_id)
        self.assertEqual(city_dict['name'], city.name)

    def test_str_representation(self):
        city = City()
        str_rep = str(city)
        self.assertTrue(isinstance(str_rep, str))
        self.assertIn(city.id, str_rep)

    
if __name__ == "__main__":
    unittest.main()
