#!/usr/bin/python3
""" Module contains class ``BaseModel`` that defines
all common attributes/methods of
other classes that will inherit fromm this class"
"""
import uuid
from datetime import datetime
# from models import storage


class BaseModel:
    """ defination of the class
    id(str): string assign with an uuid when instanve is created
    created_at(datetime): assign current datetime when instatce is created
    updated_at:(datetime) assign with current datetime when instance is updated
    """
    def __init__(self, *args, **kwargs):
        """ Initiatialize class BaseModel
        can recrete an instanace using the provided
        dictionary representation (kwargs), checks each key
        and sets corresponfing attributes
        Args:
            As defined on class defination
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        dt_v = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, dt_v)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models import storage
            # if it's new instance add it to storage
            storage.new(self)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/
        values of __dict__ of the instance
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        """returns a string representation of
        the instance in the specified format.
        """
        return "[{}] ({}) {}\n".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )
