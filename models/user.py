#!/usr/bin/ python3
"""Module contains defination class User that inherits from class BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inhgerits from BaseModel a defines user""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
