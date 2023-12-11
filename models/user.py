#!/usr/bin/python3
"""
    User module
"""

from base_model import BaseModel


class User(BaseModel):
    """
        class User:
        attributes:
        email(str): user's email
        password(str): user's acc password
        first_name(str): user's fname
        last_name(str): user's lname
    """
    email = ""
    first_name = ""
    last_name = ""
    password = ""
