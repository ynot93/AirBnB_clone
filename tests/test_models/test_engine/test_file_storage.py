#!/usr/bin/python3
"""
This module tests the operations in the File Storage class.

"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        """
        Tests the all method of FileStorage.

        """
        obj = BaseModel()
        self.file_storage.new(obj)
        objects = self.file_storage.all()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", objects)

    def test_new_method(self):
        """
        Tests the new method of FileStorage.

        """
        obj = BaseModel()
        self.file_storage.new(obj)
        objects = self.file_storage.all()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", objects)

    def test_save_and_reload_methods(self):
        """
        Tests the save and reload methods of FileStorage.

        """
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()
        self.file_storage.reload()

        objects = self.file_storage.all()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", objects)
        reloaded_obj = objects[f"{obj.__class__.__name__}.{obj.id}"]
        self.assertIsInstance(reloaded_obj, BaseModel)
        self.assertEqual(obj.to_dict(), reloaded_obj.to_dict())

    def test_classes_method(self):
        """
        Tests the classes method of FileStorage.

        """
        classes = self.file_storage.classes()
        self.assertIn('BaseModel', classes)


if __name__ == '__main__':
    unittest.main()
