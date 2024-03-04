import unittest
from models.user import User
from models.engine.file_storage import FileStorage

class TestUser(unittest.TestCase):
    """Defines the test case for the User class"""

    def setUp(self):
        """Defines the setup for the test case"""
        self.user = User()

    def tearDown(self):
        """Defines the teardown for the test case"""
        FileStorage._FileStorage__objects = {}

    def test_instance(self):
        """Test if user is an instance of User"""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test if user has all the required attributes"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_default_values(self):
        """Test if user attributes have default values"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_save(self):
        """Test if user can be saved to FileStorage"""
        self.user.save()
        self.assertIn(self.user.__class__.__name__ + '.' + self.user.id, FileStorage.all())

    def test_to_dict(self):
        """Test if user can be serialized to a dictionary"""
        serialized = self.user.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized['__class__'], 'User')
        self.assertIsNotNone(serialized['id'])
        self.assertIsNotNone(serialized['created_at'])
        self.assertIsNotNone(serialized['updated_at'])

if __name__ == '__main__':
    unittest.main()
