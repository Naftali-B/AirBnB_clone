#!/usr/bin/python3
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


if __name__ == "__main__":
    unittest.main()
