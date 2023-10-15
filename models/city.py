#!/usr/bin/python3
"""Module hasclass city defination"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel and defines city attributes.
    """
    def __init__(self, *args, **kwargs):
        """
        City class initialization.

        Args:
            state_id (str): The state ID (default is an empty string).
            name (str): The city name (default is an empty string).
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
