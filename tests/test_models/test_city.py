#!/usr/bin/python3
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

if __name__ == "__main__":
    unittest.main()
