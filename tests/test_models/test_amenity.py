#!/user/bin/python3
"""class amenity test"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    # Add tests for attributes, to_dict, and str representation

if __name__ == "__main__":
    unittest.main()
