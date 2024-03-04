import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage

class TestAmenity(unittest.TestCase):
    """Defines the test case for the Amenity class"""

    def setUp(self):
        """Defines the setup for the test case"""
        self.amenity = Amenity()

    def tearDown(self):
        """Defines the teardown for the test case"""
        FileStorage._FileStorage__objects = {}

    def test_instance(self):
        """Test if amenity is an instance of Amenity"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """Test if amenity has all the required attributes"""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_default_values(self):
        """Test if amenity attributes have default values"""
        self.assertEqual(self.amenity.name, "")

    def test_save(self):
        """Test if amenity can be saved to FileStorage"""
        self.amenity.save()
        self.assertIn(self.amenity.__class__.__name__ + '.' + self.amenity.id, FileStorage.all())

    def test_to_dict(self):
        """Test if amenity can be serialized to a dictionary"""
        serialized = self.amenity.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized['__class__'], 'Amenity')
        self.assertIsNotNone(serialized['id'])
        self.assertIsNotNone(serialized['created_at'])
        self.assertIsNotNone(serialized['updated_at'])

if __name__ == '__main__':
    unittest.main()
