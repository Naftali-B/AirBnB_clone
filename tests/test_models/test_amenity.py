#!/usr/bin/python3
<<<<<<< HEAD
"""Unittest module for the Amenity.py."""

import os
import unittest
import re
import json
from datetime import datetime
import time
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Unittests for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """test methods tear-down."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests for instantiation of Amenity class."""

        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests for the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        o = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

=======
"""
    module contains: Tests for Amenity class
"""
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """ tests class Amenity """
    def setUp(self):
        """ creates class instances """
        self.amenity = Amenity()

    def tearDown(self):
        """ deletes instance """
        del self.amenity

    def test_attributes(self):
        """ checks type and presence of attributes """
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_type_of_attributes(self):
        """ checks that attributes are the right type"""
        self.assertIsInstance(self.amenity.name, str)
>>>>>>> naf_tasks

if __name__ == "__main__":
    unittest.main()
