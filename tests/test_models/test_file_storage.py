#!/usr/bin/python3
"""Test module for FileStorage class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """defination"""
    def setUp(self):
        # Initialize a temporary test JSON file for storage
        self.test_file = "test_file.json"
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up the test JSON file after the test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_new(self):
        # Test adding a new object to storage
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), all_objs)
        self.assertEqual(all_objs["BaseModel.{}".format(obj.id)], obj)

    def test_save_and_reload(self):
        # Test saving objects to a file and reloading them
        obj1 = BaseModel()
        obj1.some_attribute = "some_value"
        obj2 = BaseModel()
        obj2.some_attribute = "some_value"

        # Add objects to storage and save to file
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        # Create a new storage instance and reload from file
        new_storage = FileStorage()
        new_storage.reload()

        # Check if objects were successfully reloaded
        all_objs = new_storage.all()
        reloaded_obj1 = all_objs["BaseModel.{}".format(obj1.id)]
        reloaded_obj2 = all_objs["BaseModel.{}".format(obj2.id)]
        self.assertEqual(reloaded_obj1.some_attribute, obj1.some_attribute)
        self.assertEqual(reloaded_obj2.some_attribute, obj2.some_attribute)


if __name__ == '__main__':
    unittest.main()
