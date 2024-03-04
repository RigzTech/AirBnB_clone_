class BaseModel:
    """A base model that provides common attributes and methods for other models."""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel with a unique ID, timestamps for creation and update."""
        self.id = None
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """A method to save the model instance."""
        # Implement your save logic here.
        # This could involve saving to a database or a file.
        pass

    def to_dict(self):
        """Returns a dictionary representation of the model."""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
