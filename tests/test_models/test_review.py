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
        Review.place_id = ""
        Review.user_id = ""
        Review.text = ""

        self.assertIsNotNone(review.id)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")


if __name__ == '__main__':
    unittest.main()
