import unittest
from models.state import State
from models.engine.file_storage import FileStorage

class TestState(unittest.TestCase):
    """Defines the test case for the State class"""

    def setUp(self):
        """Defines the setup for the test case"""
        self.state = State()

    def tearDown(self):
        """Defines the teardown for the test case"""
        FileStorage._FileStorage__objects = {}

    def test_instance(self):
        """Test if state is an instance of State"""
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """Test if state has all the required attributes"""
        self.assertTrue(hasattr(self.state, 'name'))

    def test_default_values(self):
        """Test if state attributes have default values"""
        self.assertEqual(self.state.name, "")

    def test_save(self):
        """Test if state can be saved to FileStorage"""
        self.state.save()
        self.assertIn(self.state.__class__.__name__ + '.' + self.state.id, FileStorage.all())

    def test_to_dict(self):
        """Test if state can be serialized to a dictionary"""
        serialized = self.state.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized['__class__'], 'State')
        self.assertIsNotNone(serialized['id'])
        self.assertIsNotNone(serialized['created_at'])
        self.assertIsNotNone(serialized['updated_at'])

if __name__ == '__main__':
    unittest.main()
