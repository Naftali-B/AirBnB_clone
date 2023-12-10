#!/usr/bin/python3
"""
module: class BaseModel
contains methods for persistence of data
keeps track of its number of instances
"""

from datetime import datetime
from uuid import uuid4
from models import storage

class BaseModel:
    """
    class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        initializes all instances of BaseModel
        attributes:
            id (string): unique id for every instance of BaseModel
            created_at (datetime): time at which instance was created
        """
        if kwargs:
            self.updated_at = datetime.strptime(kwargs.get('updated_at', ''),
                                                '%Y-%m-%dT%H:%M:%S.%f')
            self.created_at = datetime.strptime(kwargs.get('created_at', ''),
                                                '%Y-%m-%dT%H:%M:%S.%f')
            for k, v in kwargs.items():
                if k not in ['updated_at', 'created_at', '__class__']:
                    self.__setattr__(k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        prints a string representation of BaseClass instance
        """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict

