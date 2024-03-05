#!/usr/bin/python3

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Represents an Amenity in the AirBnB clone application.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the Amenity instance with the given attributes."""
        super().__init__(*args, **kwargs)
        if kwargs:
            for key, value in kwargs.items():
                if key == 'name':
                    self.name = value
        self.save()

    def save(self):
        """Saves the amenity instance to the storage."""
        # Implementation of saving the amenity to the storage
        pass

    def to_dict(self):
        """Returns a dictionary representation of the amenity."""
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __str__(self):
        """Returns a string representation of the amenity."""
        return "[Amenity] ({}) {}".format(self.id, self.name)
