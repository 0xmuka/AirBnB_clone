class FileStorage:
    """
     class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
    """    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ 
        returns the dictionary __objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """ 
        bla bla bla
        """
        pass
    
    def save(self):
        """ 
        bla bla bla
        """
        pass
    def reload(self):
        """ 
        bla bla bla
        """
        pass
