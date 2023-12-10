#!usr/bin/python3
"""
This module deals with attributes and methods of the
class City.

"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that contains the City information

    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a City object.

        """
        super().__init__(*args, **kwargs)
