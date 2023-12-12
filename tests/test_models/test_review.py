#!usr/bin/python3
"""
This module tests the attributes and methods of the class Review.

"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_init_default_values(self):
        """
        Test initialized values exist for Review class.

        """
        review = Review()
        review.place_id = "98765"
        review.user_id = "user456"
        review.text = "A wonderful stay at the Cozy Cottage"

        self.assertIsNotNone(review.id)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)
        self.assertEqual(review.place_id, "98765")
        self.assertEqual(review.user_id, "user456")
        self.assertEqual(review.text, "A wonderful stay at the Cozy Cottage")


if __name__ == '__main__':
    unittest.main()
