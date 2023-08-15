#!/usr/bin/python3
""" File Storage """
import os
import json


class FileStorage():
	"""Class File Storage used for serialization of instances
	to a JSON file and deserialization of JSON file to instances"""

	__file_path = 'file.json'
	__objects = {}

	def all(self):
		"""Method used to return the dictionary __objects"""

		return FileStorage.__objects
	
	def new(self, obj):
		"""Method used to set __objects with obj's class name
		and id in the form of <obj class_name>.<obj.id>"""

		FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

	def save(self):
		"""Method used to serialize __objects to the JSON file"""

		__objects_copy = {}
		for key, value in FileStorage.__objects.items():
			__objects_copy[key] = value.to_dict()
		with open(FileStorage.__file_path, "w", encoding='utf-8') as json_file:
			json.dump(__objects_copy, json_file)
	
	def reload(self):
		"""Method used to deserialize JSON file in to __objects"""
		from models.base_model import BaseModel
		from models.user import User
		from models.state import State
		from models.city import City
		from models.place import Place
		from models.amenity import Amenity
		from models.review import Review

		classes = {
					'BaseModel': BaseModel,
					'User': User,
					'State': State,
					'City': City,
					'Place': Place,
					'Amenity': Amenity,
					'Review': Review
				}
		exists = os.path.isfile(FileStorage.__file_path)
		if exists:
			with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
				for key, val in json.load(f).items():
					FileStorage.__objects[key] = classes[val['__class__']](**val)
