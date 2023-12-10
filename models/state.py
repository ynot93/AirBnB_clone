#!usr/bin/python3
"""
This modules deals with State attributes and methods.

"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class that handles the state information

    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a state object.

        """
        super().__init__(*args, **kwargs)
