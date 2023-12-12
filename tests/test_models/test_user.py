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
        User.email = "test@example.com"
        User.password = "password"
        User.first_name = "John"
        User.last_name = "Doe"

        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)
        self.assertEqual(User.email, "test@example.com")
        self.assertEqual(User.password, "password")
        self.assertEqual(User.first_name, "John")
        self.assertEqual(User.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
