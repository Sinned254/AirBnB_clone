#!/usr/bin/python3
"""Module contains clas Placedefination"""
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity


class Place(BaseModel):
    """
    Place class that inherits from BaseModel and defines place attributes.
        Place class initialization.

        Args:
            city_id (str): The City.id (default is an empty string).
            user_id (str): The User.id (default is an empty string).
            name (str): The place name (default is an empty string).
            description (str): The place description
            (default is an empty string).
            number_rooms (int): The number of rooms (default is 0).
            number_bathrooms (int): The number of bathrooms (default is 0).
            max_guest (int): The maximum number of guests (default is 0).
            price_by_night (int): The price per night (default is 0).
            latitude (float): The latitude (default is 0.0).
            longitude (float): The longitude (default is 0.0).
            amenity_ids (list): List of Amenity.id (default is an empty list).
        """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
