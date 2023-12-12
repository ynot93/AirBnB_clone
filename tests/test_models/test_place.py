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
        Place.city_id = "54321"
        Place.user_id = "user123"
        Place.name = "Cozy Cottage"
        Place.description = "A charming cottage in the woods"
        Place.number_rooms = 2
        Place.number_bathrooms = 1
        Place.max_guest = 4
        Place.price_by_night = 100
        Place.latitude = 37.7749
        Place.longitude = -122.4194
        Place.amenity_ids = ["123", "456", "789"]

        self.assertIsNotNone(place.id)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)
        self.assertEqual(Place.city_id, "54321")
        self.assertEqual(Place.user_id, "user123")
        self.assertEqual(Place.name, "Cozy Cottage")
        self.assertEqual(Place.description, "A charming cottage in the woods")
        self.assertEqual(Place.number_rooms, 2)
        self.assertEqual(Place.number_bathrooms, 1)
        self.assertEqual(Place.max_guest, 4)
        self.assertEqual(Place.price_by_night, 100)
        self.assertEqual(Place.latitude, 37.7749)
        self.assertEqual(Place.longitude, -122.4194)
        self.assertEqual(Place.amenity_ids, ["123", "456", "789"])


if __name__ == '__main__':
    unittest.main()
