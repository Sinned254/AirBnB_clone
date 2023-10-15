#!/usr/bin/python3
"""test review class Module"""
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_attributes_are_empty_strings(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
