#!/usr/bin/python3
"""test cases for class Place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()


if __name__ == "__main__":
    unittest.main()
