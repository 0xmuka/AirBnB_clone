"""import BaseModel to inheret from this"""
from models.base_model import BaseModel


class Review(BaseModel):

    place_id = ""
    user_id = ""
    text = ""
