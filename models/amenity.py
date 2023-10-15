#!/usr/bin/python3
""""Module contains class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel and defines amenity attributes.
    """
    def __init__(self, *args, **kwargs):
        """
        Amenity class initialization.

        Args:
            name (str): The amenity name (default is an empty string).
        """
        super().__init__(*args, **kwargs)
        self.name = ""
