#!/usr/bin/python3
"""
    module contains: Tests for User class
"""
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """ tests class User """
    def setUp(self):
        """ creates class instances """
        self.user = User()

    def tearDown(self):
        """ deletes instance """
        del self.user

    def test_attributes(self):
        """ checks type and presence of attributes """
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertTrue(hasattr(self.user, 'password'))

    def test_type_of_attributes(self):
        """ checks that attributes are the right type """
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.password, str)

if __name__ == "__main__":
    unittest.main()
