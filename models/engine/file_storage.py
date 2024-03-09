#!/usr/bin/python3
import json
from models.base_model import BaseModel
import os

"""Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:"""
class FileStorage():

    """
     string - path to the JSON file And dictionary - empty but will store all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

     
    def all(self):
        """
        returns the dictionary __objects
        """
        return  FileStorage.__objects
   
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        name_obj = obj.__class__.__name__
        FileStorage.__objects[f"{name_obj} {obj.id}"] = obj
    
    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        all_objects  = FileStorage.__objects
        objdict = {}
        for obj in all_objects.keys():
            objdict[obj] = all_objects[obj].to_dict()
        with open(FileStorage.__file_path, "w",encoding="utf-8") as file:
            json.dump(objdict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path,"r",encoding="utf-8") as file:
                try:
                    objdict = json.load(file)
                    for kay ,val in objdict.items():
                        class_name , objdict = kay.split(".")
                        cls = eval(class_name)
                        instance = cls(**val)
                        FileStorage.__objects[kay] = instance
                except FileNotFoundError:
                    pass




