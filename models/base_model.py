#!/usr/bin/python3
'''Base Model'''
import uuid
from datetime import datetime


class BaseModel():
    '''Base Model Class'''

    def __init__(self):
        '''init method'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''string representation'''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''save method'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''dict method'''
        diction = {}
        diction.update(self.__dict__)
        diction["__class__"] = self.__class__.__name__
        diction["created_at"] = diction["created_at"].isoformat()
        diction["updated_at"] = diction["updated_at"].isoformat()
        return diction
