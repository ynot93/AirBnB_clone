#!usr/bin/python3

from models import storage
from models.base_models import  BaseModel

Class City(BaseModel):
    """
    Class that contains the City information
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a class object
        """
        super().__init__(*args, **kwargs)
