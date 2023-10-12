#!/usr/bin/python3
""" Module contaions TestBaseModel class to run
unittest case for class BaseModel
"""
import unittest
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """defination"""
    def setUp(self):
        """Ensures each test starts from gthe same state"""
        self.base_model = BaseModel()

    def test_id_is_string(self):
        """Ensures that the id attribute is a string."""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """Checks if created_at is an instance of datetime
        """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Checks if updated_at is an instance of datetime.
        """
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Verifies that calling save updates the updated_at attribute.
        """
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dict(self):
        """Ensures that the to_dict method returns a dictionary.
        """
        data = self.base_model.to_dict()
        self.assertIsInstance(data, dict)

    def test_create_instance_with_kwargs(self):
        """tests creating a BaseModel instance with
        kwargs and verifies that the attributes are
        set correctly based on the provided data.
        """
        data = {
            'id': 'some_id',
            'created_at': '2023-10-10T12:34:56.789',
            'updated_at': '2023-10-10T12:45:23.456',
            'other_attribute': 'some_value'
        }
        base_model = BaseModel(**data)

        self.assertEqual(base_model.id, 'some_id')
        dt1 = datetime(2023, 10, 10, 12, 34, 56, 789000)
        dt2 = datetime(2023, 10, 10, 12, 45, 23, 456000)
        self.assertEqual(base_model.created_at, dt1)
        self.assertEqual(base_model.updated_at, dt2)
        self.assertEqual(base_model.other_attribute, 'some_value')

    def test_create_instance_without_kwargs(self):
        """ests creating a BaseModel instance without kwargs
        and verifies that the default values are set.
        """
        base_model = BaseModel()

        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_to_dict_contains_classname(self):
        """Checks if the returned dictionary contains the __class__ attribute.
        """
        data = self.base_model.to_dict()
        self.assertEqual(data['__class__'], 'BaseModel')

    def test_to_dict_contains_created_at(self):
        """Checks if the returned dictionary contains the created_at attribute.
        """
        data = self.base_model.to_dict()
        self.assertIn('created_at', data)

    def test_to_dict_contains_updated_at(self):
        """Checks if the returned dictionary contains the updated_at attribute.
        """
        data = self.base_model.to_dict()
        self.assertIn('updated_at', data)

    def test_str_formatting(self):
        """Verifies that the __str__ method
        produces the expected string format.
        """
        expected_str = "[BaseModel] ({}) {}\n".format(
                self.base_model.id,
                self.base_model.__dict__
                )
        self.assertEqual(str(self.base_model), expected_str)


if __name__ == '__main__':
    unittest.main()
