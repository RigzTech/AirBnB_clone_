#!/usr/bin/python3

from .user import User
from .city import City
from .state import State
from .amenity import Amenity
from .place import Place
from .review import Review

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
