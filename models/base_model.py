#!/usr/bin/python3
"""
This module defines the base model which every other class
will import from.

"""
from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """
    This class defies objects with id and datetime atributes.

    """
    def __init__(self, *args, **kwargs):
        """
        Initializes objects with the following instance attributes.

        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    setattr(
                            self,
                            key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    )
                else:
                    setattr(self, key, value)
            if 'created_at' not in kwargs or 'updated_at' not in kwargs:
                self.created_at = self.updated_at = datetime.now()
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Prints the class name, id and instance attributes as a dictionary.

        """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """
        Updates the attribute updated_at with the current datetime.

        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns dictionary with all key/values of attributes desired.

        """

        class_name = self.__class__.__name__
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = class_name
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()
        return object_dict
