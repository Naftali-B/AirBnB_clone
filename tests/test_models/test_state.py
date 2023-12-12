#!/usr/bin/python3
<<<<<<< HEAD
"""Unittest module for the State.py Class."""

import unittest
from datetime import datetime
import time
from models.state import State
import os
import json
from models.engine.file_storage import FileStorage
import re
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    """Unittests for the State class."""

    def setUp(self):
        """sets up test methods."""
        pass

    def tearDown(self):
        """Test methods tear-down."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """To reset FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Test for instantiation of State class."""

        b = State()
        self.assertEqual(str(type(b)), "<class 'models.state.State'>")
        self.assertIsInstance(b, State)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Test for the attributes of State class."""
        attributes = storage.attributes()["State"]
        o = State()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

=======
"""
    module contains: Tests for State class
"""
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """ tests class State """
    def setUp(self):
        """ creates class instances """
        self.state = State()

    def tearDown(self):
        """ deletes instance """
        del self.state

    def test_attributes(self):
        """ checks type and presence of attributes """
        self.assertTrue(hasattr(self.state, 'name'))

    def test_type_of_attributes(self):
        """ checks that attributes are the right type """
        self.assertIsInstance(self.state.name, str)
>>>>>>> naf_tasks

if __name__ == "__main__":
    unittest.main()
