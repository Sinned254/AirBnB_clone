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

    def test_to_dict_method(self):
        review_dict = self.review.to_dict()
        self.assertEqual(type(review_dict), dict)
        self.assertTrue("id" in review_dict)
        self.assertTrue("created_at" in review_dict)
        self.assertTrue("updated_at" in review_dict)
        self.assertTrue("place_id" in review_dict)
        self.assertTrue("user_id" in review_dict)
        self.assertTrue("text" in review_dict)


if __name__ == "__main__":
    unittest.main()
