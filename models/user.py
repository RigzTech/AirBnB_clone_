#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """
    Represents a User in the AirBnB clone application.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
    """
    email = ""
    password = ""
    first_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the User instance with the given attributes."""
        super().__init__(*args, **kwargs)
        if kwargs:
            for key, value in kwargs.items():
                if key == 'email':
                    self.email = value
                elif key == 'password':
                    self.password = value
                elif key == 'first_name':
                    self.first_name = value
        self.save()

    def save(self):
        """Saves the user instance to the storage."""
        # Implementation of saving the user to the storage
        pass

    def to_dict(self):
        """Returns a dictionary representation of the user."""
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __str__(self):
        """Returns a string representation of the user."""
        return "[User] ({}) {}".format(self.id, self.email)
