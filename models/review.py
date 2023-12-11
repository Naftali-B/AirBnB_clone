#!usr/bin/python3
"""
    Review
"""

from base_model import BaseModel


class Review(BaseModel):
    """
        class Review
        public attributes:
            name(str): name of review
            user(int): user_id
            name(str): text
    """

    place_id = ""
    user_id = ""
    text = ""
