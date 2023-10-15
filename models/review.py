#!/usr/bin/python3
"""Module contains class review defination"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    def to_dict(self):
        """Return a dictionary containing all attributes of the object."""
        review_dict = super().to_dict()
        review_dict['place_id'] = self.place_id
        review_dict['user_id'] = self.user_id
        review_dict['text'] = self.text
        return review_dict
