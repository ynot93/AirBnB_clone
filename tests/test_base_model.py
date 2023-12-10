#!/usr/bin/python3
"""
This module tests the functionality of the Base Model

"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    These are tests for the functions in the class BaseModel.

    """
    def test_init_default_values(self):
        """
        Test initialized values exist.

        """
        time_before_creation = datetime.now()
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        time_after_creation = datetime.now()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertTrue(time_before_creation <= my_model.created_at <= time_after_creation)
        self.assertTrue(time_before_creation <= my_model.updated_at <= time_after_creation)

    def test_save_updates_update_at(self):
        """
        Tests updated at time updates on save.

        """
        my_model = BaseModel()
        initial_updated_at_time = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at_time, my_model.updated_at)

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
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['name'], 'My First Model')
        self.assertEqual(obj_dict['my_number'], 89)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_save_method(self):
        """
        Tests the save method of BaseModel.

        """
        my_model = BaseModel()
        initial_updated_at_time = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at_time, my_model.updated_at)

    def test_init_with_kwargs(self):
        """
        Tests the __init__ method with keyword arguments.
        """
        time_before_creation = datetime.now()
        my_model = BaseModel(name="Test Model", my_number=42)
        time_after_creation = datetime.now()

        my_model_dict = my_model.to_dict()

        new_model = BaseModel(**my_model_dict)

        self.assertEqual(my_model.id, new_model.id)
        self.assertEqual(my_model.created_at, new_model.created_at)
        self.assertEqual(my_model.updated_at, new_model.updated_at)
        self.assertEqual(my_model.name, new_model.name)
        self.assertEqual(my_model.my_number, new_model.my_number)

    def test_str_method(self):
        """
        Tests the __str__ method of BaseModel.
        """
        my_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)


if __name__ == '__main__':
    unittest.main()
