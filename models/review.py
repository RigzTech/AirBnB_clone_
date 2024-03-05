#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Represents a Review in the AirBnB clone application.

    Attributes:
        place_id (str): The ID of the place the review is about.
        user_id (str): The ID of the user who made the review.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes the Review instance with the given attributes."""
        super().__init__(*args, **kwargs)
        if kwargs:
            for key, value in kwargs.items():
                if key == 'place_id':
                    self.place_id = value
                elif key == 'user_id':
                    self.user_id = value
                elif key == 'text':
                    self.text = value
        self.save()

    def save(self):
        """Saves the review instance to the storage."""
        # Implementation of saving the review to the storage
        pass

    def to_dict(self):
        """Returns a dictionary representation of the review."""
        return {
            'id': self.id,
            'place_id': self.place_id,
            'user_id': self.user_id,
            'text': self.text,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __str__(self):
        """Returns a string representation of the review."""
        return "[Review] ({}) {}".format(self.id, self.text)
