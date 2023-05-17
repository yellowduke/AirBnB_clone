#!/usr/bin/python3
"""
This Defines the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This Represent a review and it inherits from the basemodel

    Attributes:
        place_id (str): The Place id
        user_id (str): The User id
        text (str): The text of the review

    """
    place_id = ""
    user_id = ""
    text = ""
