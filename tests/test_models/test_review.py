#!/usr/bin/python3
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

if __name__ == "__main__":
    unittest.main()
