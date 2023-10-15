#!/usr/bin/python3
"""Module hasclass city defination"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel and defines city attributes.
    """
    state_id = ""
    name = ""
