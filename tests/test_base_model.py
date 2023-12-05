#!/usr/bin/python3
"""
This module tests the functionality of the Base Model

"""
import unittest
from models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    """
    These are tests for the functions in the class BaseModel.

    """
    def test_init_default_values(self):
        """
        Test initialized values exist.

        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save_updates_updatet_at(self):
        """
        Tests updated at time updates on save.

        """
        my_model = BaseModel()
        initial_updated_at_time = my_model.updated_at
        my_model.save()
        self.asertNotEqual(initial_updated_at_time, my_model.updated_at)

    def test_to_dict_methhod(self):
        """
        Tests the dictionary format of data returned by to_dict

        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        obj_dict = my_model.to_dict()
        
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('name', obj_dict)
        self.assertIn('my_number', obj_dict)

if __name__ == '__main__':
    unittest.main()
