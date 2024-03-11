#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.
    Attributes:
        place_id is 'str' => The Place id.
        user_id  is 'str' => The User id.
        text  is 'str' => The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""