#!/usr/bin/python3
"""
This module tests the functionality of the City Model

"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_init_default_values(self):
        """
        Test initialized values exist for City class.

        """
        city = City()
        City.state_id = "12345"
        City.name = "San Francisco"

        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)
        self.assertEqual(City.state_id, "12345")
        self.assertEqual(City.name, "San Francisco")


if __name__ == '__main__':
    unittest.main()
