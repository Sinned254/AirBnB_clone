#!/usr/bin/python3
"""Module contains class review defination"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    place_id = ""
    user_id = ""
    text = ""
