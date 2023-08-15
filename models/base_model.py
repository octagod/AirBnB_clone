#!/usr/bin/python3
""" Base Model """
import uuid
from datetime import datetime
from models import storage


class BaseModel():
	""" Base Model Class """

	def __init__(self, *args, **kwargs):
		""" __init__ Attribute """
		
		if kwargs:
			for key in kwargs:
				if key == "__class__":
					continue
				
				if key == "created_at":
					self.__dict__["created_at"] = datetime.strptime(
						kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
				elif key == "updated_at":
					self.__dict__["updated_at"] = datetime.strptime(
						kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
				else:
					self.__dict__[key] = kwargs[key]
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			storage.new(self)

	def __str__(self):
		""" string representation attribute """
		
		return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

	def save(self):
		""" Save method """
		
		self.updated_at = datetime.now()
		storage.save()

	def to_dict(self):
		""" dict method """
		
		diction = {}
		diction.update(self.__dict__)
		diction["__class__"] = self.__class__.__name__
		diction["created_at"] = diction["created_at"].isoformat()
		diction["updated_at"] = diction["updated_at"].isoformat()
		return diction
