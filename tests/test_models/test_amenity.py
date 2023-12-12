#!/usr/bin/python3
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

if __name__ == "__main__":
    unittest.main()
