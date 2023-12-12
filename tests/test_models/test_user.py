#!/usr/bin/python3
"""
This module tests the functionality of the User Model

"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_init_default_values(self):
        """
        Test initialized values exist for User class.

        """
        user = User()

        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
