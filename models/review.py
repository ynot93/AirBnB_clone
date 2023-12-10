#!usr/bin/python3
"""
This module deals with attributes and methods of the
class Review.

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class that handles the review information

    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a Review object.

        """

        super().__init__(*args, **kwargs)
