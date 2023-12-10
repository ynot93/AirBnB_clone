#!usr/bin/python3
"""
This module tests the functionality of the class Place.

"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_init_default_values(self):
        """
        Test initialized values exist for Place class.

        """
        place = Place()
        place.city_id = "54321"
        place.user_id = "user123"
        place.name = "Cozy Cottage"
        place.description = "A charming cottage in the woods"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["123", "456", "789"]

        self.assertIsNotNone(place.id)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)
        self.assertEqual(place.city_id, "54321")
        self.assertEqual(place.user_id, "user123")
        self.assertEqual(place.name, "Cozy Cottage")
        self.assertEqual(place.description, "A charming cottage in the woods")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["123", "456", "789"])


if __name__ == '__main__':
    unittest.main()
