from models.base_model import BaseModel

class City(BaseModel):
    """Represents a City in the AirBnB clone application.

    Attributes:
        name (str): The name of the city.
        state_id (str): The ID of the state the city belongs to.
    """
    name = ""
    state_id = ""

