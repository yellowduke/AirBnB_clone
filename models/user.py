#!/usr/bin/python3
"""
This Defines the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This Represents a User and inherits from the basemodel

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
