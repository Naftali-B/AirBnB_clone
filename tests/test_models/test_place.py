#!/usr/bin/python3
<<<<<<< HEAD
"""File defining unittests for models/place.py."""

import os
import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    """test Cases for the Place class."""

    def setUp(self):
        """sets up test methods."""
        pass

    def tearDown(self):
        """Test methods tear-down."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Unittests for instantiation of Place class."""

        b = Place()
        self.assertEqual(str(type(b)), "<class 'models.place.Place'>")
        self.assertIsInstance(b, Place)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests for attributes of Place class."""
        attributes = storage.attributes()["Place"]
        o = Place()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

=======
"""
    module contains: Tests for Place class
"""
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """ tests class Place """
    def setUp(self):
        """ creates class instances """
        self.place = Place()

    def tearDown(self):
        """ deletes instance """
        del self.place

    def test_attributes(self):
        """ checks type and presence of attributes """
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_type_of_attributes(self):
        """ checks that attributes are the right type """
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)
>>>>>>> naf_tasks

if __name__ == "__main__":
    unittest.main()
