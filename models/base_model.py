#!/usr/bin/python3
"""
"""
import uuid
import models
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for kay, value in kwargs.items():
                if kay == __class__:
                    continue
                elif kay == "created_at" or kay == "updated_at":
                    self.__dict__[kay] = datetime.strptime(value, tform)
                else:
                    self.__dict__[kay] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
        models.storage.new(self)  

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.save()
    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """  
        inst_dic = self.__dict__
        instanc_dict = inst_dic.copy()
        instanc_dict["__class__"] = self.__class__.__name__
        instanc_dict["created_at"] = self.created_at.isoformat()
        instanc_dict["updated_at"] = self.updated_at.isoformat()

        return instanc_dict
    def __str__(self) -> str:
        """Return the print/str representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
    
