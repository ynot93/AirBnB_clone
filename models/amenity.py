#!usr/bin/python3
"""
This module deals with attributes and methods of the
class Amenity.

"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class that contains the Amenity information

    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes an Amenity object.

        """
        super().__init__(*args, **kwargs)
