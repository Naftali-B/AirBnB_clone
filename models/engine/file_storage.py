#!/usr/bin/python3
"""
    FileStorage module
"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

class FileStorage:
    """
    A class for handling the storage of objects in a JSON file.
    """

    def __init__(self, file_path='file.json'):
        """
        Initialize the FileStorage instance with the specified file path.
        """
        self.__file_path = file_path
        self.__objects = {}
        self.classes = {"BaseModel": BaseModel,
                        "State": State,
                        "City": City,
                        "Amenity": Amenity,
                        "Place": Place,
                        "Review": Review,
                        "User": User}

    def all(self):
        """Return the dictionary of stored objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        my_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, mode='w', encoding='UTF-8') as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserialize the JSON file back into objects."""
        try:
            with open(self.__file_path, mode="r") as f:
                new_dict = json.load(f)
                for k, v in new_dict.items():
                    class_name = v.get("__class__")
                    if class_name and class_name in self.classes:
                        base = self.classes[class_name](**v)
                        self.__objects[k] = base
        except FileNotFoundError:
            print(f"File not found: {self.__file_path}")
