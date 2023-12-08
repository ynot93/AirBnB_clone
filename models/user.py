#!usr/bin/python3

from models import storage
from models.base_model import BaseModel

Class User(BaseModel):

    """
    Class that handles the users information
    """

    email = ""
    pasword = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes  a class object
        """
        super().__init__(*args, **kwargs)
