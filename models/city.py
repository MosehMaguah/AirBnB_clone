#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class is for managing city objects"""

    state_id = ''
    name = ''
