import models
import uuid
from datetime import datetime

class BaseModel:
    """Base Model for project"""
    
    def __init__(self):
        """Intialize a Base Model"""
        self.id = str(uuid.uuid4)