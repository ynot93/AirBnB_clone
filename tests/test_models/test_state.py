#!/usr/bin/python3
"""
This module tests the functionality of the State Model

"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_init_default_values(self):
        """
        Test initialized values exist for State class.

        """
        state = State()
        state.name = "California"

        self.assertIsNotNone(state.id)
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)
        self.assertEqual(state.name, "California")


if __name__ == '__main__':
    unittest.main()
