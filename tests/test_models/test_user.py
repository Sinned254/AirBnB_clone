#!/usr/bin/python3
"""Module has class Test User to run test un class user
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test class User"""

    def setUp(self):
        self.user = User()

    def test_attributes_are_empty_strings(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_setting_attributes(self):
        self.user.email = "user@example.com"
        self.user.password = "secret"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "user@example.com")
        self.assertEqual(self.user.password, "secret")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_str_representation(self):
        # Set the attributes of the User instance
        self.user.email = "user@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        # Get the string representation
        str_representation = str(self.user)
        # Check if specific attributes are present in the string representation
        self.assertIn(f"[User] ({self.user.id})", str_representation)
        self.assertIn(f"'email': 'user@example.com'", str_representation)
        self.assertIn(f"'password': 'password123'", str_representation)
        self.assertIn(f"'first_name': 'John'", str_representation)
        self.assertIn(f"'last_name': 'Doe'", str_representation)


if __name__ == '__main__':
    unittest.main()
