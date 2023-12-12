#!/usr/bin/python3
<<<<<<< HEAD
"""Unittests for models/city.py."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """Unittest for the City class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets for FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Unittest for instantiation of City class."""

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests for attributes of City class."""
        attributes = storage.attributes()["City"]
        o = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

=======
"""
    module contains: Tests for City class
"""
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """ tests class City """
    def setUp(self):
        """ creates class instances """
        self.city = City()

    def tearDown(self):
        """ deletes instance """
        del self.city

    def test_attributes(self):
        """ checks type and presence of attributes """
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))

    def test_type_of_attributes(self):
        """ checks that attributes are the right type """
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)
>>>>>>> naf_tasks

if __name__ == "__main__":
    unittest.main()
