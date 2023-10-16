#!/usr/bin/python3
"""test cases for class Place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_default_city_id(self):
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_default_user_id(self):
        place = Place()
        self.assertEqual(place.user_id, "")

    def test_default_name(self):
        place = Place()
        self.assertEqual(place.name, "")


if __name__ == "__main__":
    unittest.main()
