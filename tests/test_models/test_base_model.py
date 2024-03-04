import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """Defines the test case for the BaseModel class"""

    def setUp(self):
        """Defines the setup for the test case"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Defines the teardown for the test case"""
        FileStorage._FileStorage__objects = {}

    def test_instance(self):
        """Test if base_model is an instance of BaseModel"""
        self.assertIsInstance(self.base_model, BaseModel)

    def test_attributes(self):
        """Test if base_model has all the required attributes"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_default_values(self):
        """Test if base_model attributes have default values"""
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)

    def test_save(self):
        """Test if base_model can be saved to FileStorage"""
        self.base_model.save()
        self.assertIn(self.base_model.__class__.__name__ + '.' + self.base_model.id, FileStorage.all())

    def test_to_dict(self):
        """Test if base_model can be serialized to a dictionary"""
        serialized = self.base_model.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized['__class__'], 'BaseModel')
        self.assertIsNotNone(serialized['id'])
        self.assertIsNotNone(serialized['created_at'])
        self.assertIsNotNone(serialized['updated_at'])

if __name__ == '__main__':
    unittest.main()
