#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Represents a Place in the AirBnB clone application.

    Attributes:
        name (str): The name of the place.
        description (str): A short description of the place.
        price_by_night (float): The price for one night's stay.
        address (str): The address of the place.
        city_id (str): The ID of the city where the place is located.
        amenity_ids (list): A list of amenity IDs associated with the place.
    """
    name = ""
    description = ""
    price_by_night = 0.0
    address = ""
    city_id = ""
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initializes the Place instance with the given attributes."""
        super().__init__(*args, **kwargs)
        if kwargs:
            for key, value in kwargs.items():
                if key == 'name':
                    self.name = value
                elif key == 'description':
                    self.description = value
                elif key == 'price_by_night':
                    self.price_by_night = value
                elif key == 'address':
                    self.address = value
                elif key == 'city_id':
                    self.city_id = value
                elif key == 'amenity_ids':
                    self.amenity_ids = value
        self.save()

    def save(self):
        """Saves the place instance to the storage."""
        # Implementation of saving the place to the storage
        pass

    def to_dict(self):
        """Returns a dictionary representation of the place."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price_by_night': self.price_by_night,
            'address': self.address,
            'city_id': self.city_id,
            'amenity_ids': self.amenity_ids,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __str__(self):
        """Returns a string representation of the place."""
        return "[Place] ({}) {}".format(self.id, self.name)
