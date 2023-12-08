#!usr/bin/python3

from models import storage
from models.base_model import BaseModel

Class Review(BaseModel):
    """
    Class that handles the review information
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a class object
        """

        super().__init__(*args, **kwargs)
