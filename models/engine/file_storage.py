class FileStorage:
    """
        Class FileStorage serializes instances
        to a JSON file and deserializes JSON file to instances
    """
    __FILE_PATH = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__class__.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__class__.__objects[key] = obj

    def save(self):
        """Save serialized objects to a JSON file."""
        pass

    def reload(self):
        """Reload objects from a JSON file."""
        pass
