import unittest
from models.review import Review
from models.engine.file_storage import FileStorage

class TestReview(unittest.TestCase):
    """Defines the test case for the Review class"""

    def setUp(self):
        """Defines the setup for the test case"""
        self.review = Review()

    def tearDown(self):
        """Defines the teardown for the test case"""
        FileStorage._FileStorage__objects = {}

    def test_instance(self):
        """Test if review is an instance of Review"""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """Test if review has all the required attributes"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_default_values(self):
        """Test if review attributes have default values"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_save(self):
        """Test if review can be saved to FileStorage"""
        self.review.save()
        self.assertIn(self.review.__class__.__name__ + '.' + self.review.id, FileStorage.all())

    def test_to_dict(self):
        """Test if review can be serialized to a dictionary"""
        serialized = self.review.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized['__class__'], 'Review')
        self.assertIsNotNone(serialized['id'])
        self.assertIsNotNone(serialized['created_at'])
        self.assertIsNotNone(serialized['updated_at'])

if __name__ == '__main__':
    unittest.main()
