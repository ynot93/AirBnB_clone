#!/usr/bin/python3
"""
This module defines the base model which every other class
will import from.

"""
from datetime import datetime
import uuid


class BaseModel():
    """
    This class defies objects with id and datetime atributes.

    """
    def __init__(self, name=None, my_number=None, id=None, created_at=None, updated_at=None):
        """
        Initializes objects with the following instance attributes.

        """
        self.name = name
        self.my_number = my_number
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Prints the class name, id and instance attributes as a dictionary.

        """
        class_name =  self.__class__.__name__
        print("")

    def save(self):
        """
        Updates the attribute updated_at with the current datetime.

        """

    def to_dict(self):
        """
        Returns dictionary with all key/values of attributes desired.

        """
        return {
            'my_number': self.my_number,
            'name': self.my_name,
            '__class__': self.__class__.__name__,
        }


