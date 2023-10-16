#!/user/bin/python3
"""class amenity test"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_default_name(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_set_name(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")


if __name__ == "__main__":
    unittest.main()
