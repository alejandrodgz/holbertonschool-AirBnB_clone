#!/usr/bin/python3
"""this module contains the class Review
that inherits from class BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """the class defines Review

    Public class attributes:
        place_id (str): The id of the place of the review.
        user_id (str): The id of the user of the review.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
