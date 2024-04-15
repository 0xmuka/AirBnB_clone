import uuid
from datetime import datetime as dt


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = dt.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = dt.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        self.updated_at = dt.now()

    def to_dict(self):
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj


x = BaseModel()
print(x.to_dict())
