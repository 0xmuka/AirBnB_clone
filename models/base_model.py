#!/usr/bin/python3
"""
BaseModel
"""


import uuid
from datetime import datetime as dt
from models import storage


class BaseModel:
    """all function in basemodel class"""

    def __init__(self, *args, **kwargs):
        """id / created_at / updated_at"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' in key:
                self.created_at.isoformat()
            if 'updated_at' in key:
                self.updated_at.isoformat()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        """ {[<class name>] (<self.id>) <self.__dict__>}"""
        return ("[{}] ({}) {}").format(
          self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        update
        """
        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """
        copy a dictionary and return new values
        """
        my_ob_dict = self.__dict__.copy()
        my_ob_dict["__class__"] = self.__class__.__name__
        my_ob_dict["created_at"] = my_ob_dict["created_at"].isoformat()
        my_ob_dict["updated_at"] = my_ob_dict["updated_at"].isoformat()
        return my_ob_dict
