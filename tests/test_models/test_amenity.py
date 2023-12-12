#!usr/bin/python3
"""
This module tests attributes and methods of the class Amenity.

"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_init_default_values(self):
        """
        Test initialized values exist for Amenity class.

        """
        amenity = Amenity()
        Amenity.name = "WiFi"

        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)
        self.assertEqual(Amenity.name, "WiFi")


if __name__ == '__main__':
    unittest.main()
