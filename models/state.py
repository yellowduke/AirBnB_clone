#!/usr/bin/python3
"""
This Defines the State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """This Represents a state and it inherits from the basemodel
    Attributes:
        name (str): The name of the state

    """
    name = ""
