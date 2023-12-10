#!/usr/bin/python3
"""
This module deals with the storage and retrieval of json
data to and from a file.

"""
import json
from os.path import isfile


class FileStorage():
    """
    Serializes and desrializes instances to and from JSON files.

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects.

        """
        return self.__objects

    def classes(self):
        """
        Returns list of available classes.

        """
        classes = {
                'BaseModel',
                'User',
                'State',
                'City',
                'Amenity',
                'Place',
                'Review'
        }
        for key in self.__objects.keys():
            class_name, _ = key.split('.')
            classes.add(class_name)
        return list(classes)

    def new(self, obj):
        """
        Populates __objects with obj using key classname.id

        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Converts the dict __objects to a JSON file.

        """
        dict_objects = {
                key: obj.to_dict() for key, obj in self.__objects.items()
        }
        with open(self.__file_path, 'w') as file:
            json.dump(dict_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.

        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        if isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                objects = json.load(file)
                for key, obj_dict in objects.items():
                    class_name, obj_id = key.split('.')
                    obj_class = eval(class_name)
                    obj_instance = obj_class(**obj_dict)
                    self.__objects[key] = obj_instance
