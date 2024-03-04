from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a Review in the AirBnB clone application.

    Attributes:
        place_id (str): The ID of the place the review is about.
        user_id (str): The ID of the user who made the review.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""

