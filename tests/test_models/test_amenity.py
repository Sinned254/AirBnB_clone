#!/user/bin/python3
"""class amenity test"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()


if __name__ == "__main__":
    unittest.main()
