import uuid
from datetime import datetime as dt


class BaseModel:
    """
    aykalam
    """
    def __init__(self) -> None:
        """
        initialization
        """
        self.id = str(uuid.uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()

    def __str__(self) -> str:
        return f"{[__class__.__name__]} {(self.id)} {self.__dict__}"

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
