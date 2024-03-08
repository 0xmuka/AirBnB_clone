import models
import uuid
from datetime import datetime

class BaseModel:
    """Base Model for project"""
    
    def __init__(self):
        """Intialize a Base Model"""
        self.id = str(uuid.uuid4)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        
    def __str__(self) -> str:
        """ 
             should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}").format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()
        
    def to_dict(self):
            pass