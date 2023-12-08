#!usr/bin/python3

from models import storage
from models.base_model import BaseModel

Class State(BaseModel):
    """
    Class that handles the state information
    """

    name = ""

    def __init__(self, *args, **kwargs):

    """
    Initializes a class object
    """

    super().__init__(*args, **kwargs)
