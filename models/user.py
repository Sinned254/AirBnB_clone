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

    def __init__(self, *args, **kwargs):
        """class user initialization,
        args: email, passowrd, first_name, last_name"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
    
    def to_dict(self):
        """
        Return a dictionary representation of the User instance.
        """
        # Call the to_dict method of the base class to get the common attributes
        user_dict = super().to_dict()

        # Add the attributes specific to the User class
        user_dict['email'] = self.email
        user_dict['password'] = self.password
        user_dict['first_name'] = self.first_name
        user_dict['last_name'] = self.last_name

        return user_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """
        Creates a User instance from a dictionary.
        
        Args:
            data (dict): A dictionary containing User attributes.

        Returns:
            User: An instance of the User class.
        """
        super().from_dict(obj_dict)
        self.email = obj_dict.get('email', "")
        self.password = obj_dict.get('password', "")
        self.first_name = obj_dict.get('first_name', "")
        self.last_name = obj_dict.get('last_name', "")
        self.is_user = obj_dict.get('is_user', True)
