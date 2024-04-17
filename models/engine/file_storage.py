"""Import Json to serializes and deserializes"""

import json
import os
from datetime import datetime


class FileStorage:
    """ File Storage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return empty dictionary"""
        return self.__objects

    def new(self, obj):
        """Create new object"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):

        """convert dictionary to json file string"""
        with open(FileStorage.__file_path, 'w', encoding="utf8") as f:
            json_str = {key: value.to_dict()
                        for key, value in self.__objects.items()}
            json.dump(json_str, f)

    def reload(self):
        """ reload json string from """
        from models.base_model import BaseModel
        from models.user import User
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }

        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value.get('__class__')
                    if class_name in classes:
                        # Convert 'created_at' and '
                        # updated_at' strings to datetime objects
                        value['created_at'] = datetime.fromisoformat(
                            value['created_at'])
                        value['updated_at'] = datetime.fromisoformat(
                            value['updated_at'])

                        # Create an instance of
                        # the class and add it to __objects
                        obj = classes[class_name](**value)
                        FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def classes(self):
        """
        serialize and deserialize instances of the new classes
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        return classes
