#!/usr/bin/python3
import os
import uuid
import json


class FileStorage:
    """A simple file storage system."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""

        filedata = {}
        for key, obj in self.__objects.items():
            filedata[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(filedata, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = eval(class_name)
                    obj = class_obj(**obj_data)
                    self.__objects[key] = obj
