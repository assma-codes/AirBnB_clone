#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.
    Attributes:
        state_id is 'str'=> The state id.
        name is 'str'=>  The name of the city.
    """

    state_id = ""
    name = ""