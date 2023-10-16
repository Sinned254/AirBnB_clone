#!/usr/bin/python3
"""Module conatains class FileStorage that serializes
instances to a JSON file and deserializes JSON file to instances:
"""
from models.base_model import BaseModel
import json
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.state import State


class FileStorage:
    """Class serializes insatnces to JSON file and
    deserializea JSON file to instances
    ARgs:
        __file_path: private class atribute string -
        path to the JSON file (ex: file.json)
        __objects: dictionary -private class attribute
        empty but will store all objects by
    Methods:
        all(self):
        new(self, obj):
        save(self):
        reload(self):
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing).
        If the file doesn’t exist, no exception should be raised.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for obj_dict in json_dict.values():
                    cls = obj_dict['__class__']
                    self.new(eval('{}({})'.format(cls, '**obj_dict')))

        except FileNotFoundError:
            pass
