#!/usr/bin/python3

import datetime
import uuid


class BaseModel:
    """
    attributes and methods for models in the AirBnB clone application.

    Attributes:
        id (str): A unique identifier for each instance of the model.
        created_at (datetime): time created.
        updated_at (datetime): time last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel instance with a
        unique ID and timestamps for creation and update.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.save()

    def save(self):
        """A method to save the model instance."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the model.
        """
        model_dict = self.__dict__

        for key in model_dict:
            if key in ["created_at", "updated_at"]:
                model_dict[key] = model_dict[key].isoformat()

        model_dict["__class__"] = self.__class__.__name__
        return model_dict

    def __str__(self):
        """
        Returns a string representation of the model.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )
