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

        classes = {'BaseModel': BaseModel,
                   'User': User}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf8") as f:
                data = json.load(f)
                for key, value in data.items():
                    # Convert 'created_at' and 'updated_at'
                    # strings to datetime objects all right
                    value['created_at'] = datetime.fromisoformat(
                        value['created_at'])
                    value['updated_at'] = datetime.fromisoformat(
                        value['updated_at'])
                    # Ensure the class name exists in the dictionary
                    class_name = value.get('__class__')
                    if class_name and class_name in classes:
                        FileStorage.__objects[key] = classes[class_name](**value)
                    else:
                        print("Unknown class:", class_name)
        else:
            return

    def classes(self):
        """
        to correctly serialize and deserialize instances of the new classes
        """
        from models.base_model import BaseModel
        classes = {
            "BaseModel": BaseModel
        }
        return classes
