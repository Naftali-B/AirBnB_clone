#!/usr/bin/python3
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

if __name__ == "__main__":
    unittest.main()
