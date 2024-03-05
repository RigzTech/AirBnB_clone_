#!/usr/bin/python3

import datetime

class BaseModel:
    """
    Provides common attributes and methods for all models in the AirBnB clone application.

    Attributes:
        id (str): A unique identifier for each instance of the model.
        created_at (datetime): The timestamp for when the instance was created.
        updated_at (datetime): The timestamp for when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel instance with a unique ID and timestamps for creation and update."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.save()

    def save(self):
        """A method to save the model instance."""
        # Implementation of save logic here.
        # This could involve saving to a database or a file.
        pass

    def to_dict(self):
        """Returns a dictionary representation of the model."""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __str__(self):
        """Returns a string representation of the model."""
        return "[{}] ({})".format(self.__class__.__name__, self.id)
