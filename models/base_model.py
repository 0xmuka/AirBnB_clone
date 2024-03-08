import models
import uuid
from datetime import datetime

class BaseModel:
    """Base Model for project"""
    
    def __init__(self, *args, **kwargs):
        """Initialize a Base Model"""
        if kwargs:
            if '__class__' in kwargs:
                kwargs.pop('__class__')  # Remove __class__ key if present
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4)
            
            
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        
    def __str__(self) -> str:
        """ 
             should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}").format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """bla bal"""
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """bla bla bla"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    