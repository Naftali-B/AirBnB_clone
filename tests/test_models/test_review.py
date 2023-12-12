#!/usr/bin/python3
<<<<<<< HEAD
"""Unittest module for the Review.py."""
import os
import unittest
from datetime import datetime
import time
import re
from models.review import Review
import json
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    """test Cases for the Review class."""

    def setUp(self):
        """Set up test methods."""
        pass

    def tearDown(self):
        """Tear down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Test instantiation of Review class."""

        b = Review()
        self.assertEqual(str(type(b)), "<class 'models.review.Review'>")
        self.assertIsInstance(b, Review)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Test the attributes of Review class."""
        attributes = storage.attributes()["Review"]
        o = Review()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

=======
"""
    module contains: Tests for Review class
"""
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """ tests class Review """
    def setUp(self):
        """ creates class instances """
        self.review = Review()

    def tearDown(self):
        """ deletes instance """
        del self.review

    def test_attributes(self):
        """ checks type and presence of attributes """
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))

    def test_type_of_attributes(self):
        """ checks that attributes are the right type """
        self.assertIsInstance(self.review.text, str)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
>>>>>>> naf_tasks

if __name__ == "__main__":
    unittest.main()
