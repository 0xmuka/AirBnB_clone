import uuid
from datetime import datetime as dt
from models import fs


class BaseModel:

    def __init__(self, *args, **kwargs) -> None:
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
            fs.new(self)

    def __str__(self) -> str:
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = dt.now()
        fs.save()

    def to_dict(self):
        object = self.__dict__.copy()
        object['__class__'] = self.__class__.__name__
        object['created_at'] = self.created_at.isoformat()
        object['updated_at'] = self.updated_at.isoformat()
        return object
