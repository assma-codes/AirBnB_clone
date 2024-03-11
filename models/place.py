#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place."""
    """"
    Attributes:
        city_id is 'str'=> The City id.
        user_id is 'str'=> The User id.
        name is 'str' => The name of the place.
        description is 'str' => The description of the place.
        number_rooms is 'int' => The number of rooms of the place.
        number_bathrooms is 'str' => The number of bathrooms of the place.
        max_guest is 'str' => The maximum number of guests of the place.
        price_by_night is 'str' => The price by night of the place.
        latitude is 'str' => The latitude of the place.
        longitude is 'str' => The longitude of the place.
        amenity_ids is 'str' => A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
