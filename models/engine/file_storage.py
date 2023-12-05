#!/usr/bin/python3
"""
This module deals with the storage and retrieval of json
data to and from a file.

"""
import json


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

    def new(self, obj):
        """
        Populates __objects with obj using key classname.id

        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Converts the dict __objects to a JSON file.

        """
        dict_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(dict_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.

        """
        if __file_path:
            with open(self.__file_path, 'r') as file:
                objects = json.load(file)
                for key, obj_dict in objects.items():
                    class_name, obj.id = key.split('.')
                    obj_class = getattr(models, class_name)
                    obj_instance = obj_class(**obj_dict)
                    self.__objects[key] = obj_instance
