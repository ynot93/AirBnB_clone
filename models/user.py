#!usr/bin/python3
"""
This module deals with anything User related.

"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that handles the users information

    """

    email = ""
    pasword = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a User class object.

        """
        super().__init__(*args, **kwargs)
