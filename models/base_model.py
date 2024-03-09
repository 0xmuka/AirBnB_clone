import models
import uuid
from datetime import datetime


class BaseModel:
    """Base Model for project"""

    def __init__(self, *args, **kwargs):
        """Initialize a Base Model"""

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Should print: [<class name>] (<self.id>) <self.__dict__>"""
        return ("[{}] ({}) {}").format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute to current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
