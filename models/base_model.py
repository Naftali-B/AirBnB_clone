#!/usr/bin/python3
"""
module: class BaseModel
contains methods for persistence of data
keeps track of it's number of instances
"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
        class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
            initializes all instances of BaseModel
            attributes:
                id(string): unique id for every instance of BaseModel
                created_at(datetime): time at which instance was created
        """
        if kwargs:
            self.updated_at = datetime.\
                strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.created_at = datetime.\
                strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for k, v in kwargs.items():
                if k not in ['updated_at', 'created_at', '__class__']:
                    self.__setattr__(k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            prints a string representation of BaseClass instance
        """
        return '[{}] ({}) {}'\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        dict = self.__dict__.copy()
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict
