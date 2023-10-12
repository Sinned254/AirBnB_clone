#!/usr/bin/ python3
"""Module contains defination class User that inherits from class BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inhgerits from BaseModel a defines user"""
    def __init__(self, *args, **kwargs):
        """class user initialization, 
        args: email, passowrd, first_name, last_name"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
