#!/usr/bin/python3

from models.base_model import BaseModel

class City(BaseModel):
    """
    Represents a City in the AirBnB clone application.

    Attributes:
        name (str): The name of the city.
        state_id (str): The ID of the state where the city is located.
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes the City instance with the given attributes."""
        super().__init__(*args, **kwargs)
        if kwargs:
            for key, value in kwargs.items():
                if key == 'name':
                    self.name = value
                elif key == 'state_id':
                    self.state_id = value
        self.save()

    def save(self):
        """Saves the city instance to the storage."""
        # Implementation of saving the city to the storage
        pass

    def to_dict(self):
        """Returns a dictionary representation of the city."""
        return {
            'id': self.id,
            'name': self.name,
            'state_id': self.state_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __str__(self):
        """Returns a string representation of the city."""
        return "[City] ({}) {}".format(self.id, self.name)
