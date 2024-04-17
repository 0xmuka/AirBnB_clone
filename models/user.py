""""import BaseModel to inhert from it"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
