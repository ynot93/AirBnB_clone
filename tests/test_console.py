#!/usr/bin/python3
"""
This module deals with unittests for the command line
interface that runs our HBNB application.

"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import os
import re


class TestHBNBCommand(unittest.TestCase):

    def test_create(self):
        command = "create BaseModel"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        uuid_pattern = re.compile(
                r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-'
                r'[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'
        )

        actual_output = mock_stdout.getvalue().strip()
        self.assertTrue(
            bool(uuid_pattern.match(actual_output))
        )

    def test_create_missing_class_name(self):
        command = "create"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** class name missing **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_create_invalid_class_name(self):
        command = "create MyModel"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** class doesn't exist **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_show_missing_class_name(self):
        command = "show"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** class name missing **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_show_invalid_class_name(self):
        command = "show MyModel"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** class doesn't exist **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_show_missing_id(self):
        command = "show BaseModel"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** instance id missing **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_quit(self):
        command = "quit"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = ""
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_show_invalid_id(self):
        command = "show BaseModel 121212"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** no instance found **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_destroy_missing_class_name(self):
        command = "destroy"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** class name missing **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_destroy_invalid_class_name(self):
        command = "destroy MyModel"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** class doesn't exist **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_destroy_missing_id(self):
        command = "destroy BaseModel"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** instance id missing **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_destroy_invalid_id(self):
        command = "destroy BaseModel 121212"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** no instance found **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_all_base_model(self):
        command = "all BaseModel"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "[BaseModel]"
        actual_output = mock_stdout.getvalue().strip()

        self.assertIn(expected_output, actual_output)

    def test_all_missing_class_name(self):
        command = "all"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "[BaseModel]"
        actual_output = mock_stdout.getvalue().strip()

        self.assertIn(expected_output, actual_output)

    def test_all_invalid_class_name(self):
        command = "all MyModel"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** class doesn't exist **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_update_missing_class_name(self):
        command = "update"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** class name missing **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_update_invalid_class_name(self):
        command = "update MyModel"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** class doesn't exist **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_update_missing_id(self):
        command = "update BaseModel"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** instance id missing **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_update_invalid_id(self):
        command = "update BaseModel 121212"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** no instance found **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_update_missing_attribute_name(self):
        command = "update BaseModel c574cfde-95cd-4c3b-b501-1f702243b8ae"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** attribute name missing **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)

    def test_update_missing_value(self):
        command = ("update BaseModel "
                   "c574cfde-95cd-4c3b-b501-1f702243b8ae "
                   "first_name")
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd(command)

        expected_output = "** value missing **"
        actual_output = mock_stdout.getvalue().strip()

        self.assertEqual(expected_output, actual_output)




if __name__ == "__main__":
    unittest.main()
