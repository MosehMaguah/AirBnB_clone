#!/usr/bin/python3
'''This module creates a User class'''
from models.base_model import BaseModel


class City(BaseModel):
    '''This Class is for managing city objects'''
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the city class'''
        super().__init__(*args, **kwargs)
