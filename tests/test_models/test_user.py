#!/usr/bin/python3
<<<<<<< HEAD
"""Unittests module for the User.py class."""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """Test cases for User class."""

    def setUp(self):
        """To set up test methods."""
        pass

    def tearDown(self):
        """tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests the instantiation of User class."""

        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests for the attributes of User class."""
        attributes = storage.attributes()["User"]
        o = User()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

=======
"""
    module contains: Tests for User class
"""
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """ tests class User """
    def setUp(self):
        """ creates class instances """
        self.user = User()

    def tearDown(self):
        """ deletes instance """
        del self.user

    def test_attributes(self):
        """ checks type and presence of attributes """
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertTrue(hasattr(self.user, 'password'))

    def test_type_of_attributes(self):
        """ checks that attributes are the right type """
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.password, str)
>>>>>>> naf_tasks

if __name__ == "__main__":
    unittest.main()
