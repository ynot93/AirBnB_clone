#!usr/bin/python3

from models import storage
from models.base_model import BaseModel
from models.user import User

#all_objs = storage.all()
#print("-- Reloaded objects --")
#for obj_id in all_objs.keys():
    #obj = all_objs[obj_id]
    # print(obj)

Class user(BaseModel):

    """
    Class that handles the users information
    """

    email = ""
    pasword = ""
    first_name = ""
    last_name = ""
