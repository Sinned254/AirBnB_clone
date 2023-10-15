#!/bin/bash/python3
"""conatins class state defination"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel
    and defines a state with a name."""
    def __init__(self, *args, **kwargs):
        """Initialize the State instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
