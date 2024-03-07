# #!/usr/bin/python3

# import unittest
# from models.city import City
# from models.engine.file_storage import FileStorage

# class TestCity(unittest.TestCase):
#     """Defines the test case for the City class"""

#     def setUp(self):
#         """Defines the setup for the test case"""
#         self.city = City()

#     def tearDown(self):
#         """Defines the teardown for the test case"""
#         FileStorage._FileStorage__objects = {}

#     def test_instance(self):
#         """Test if city is an instance of City"""
#         self.assertIsInstance(self.city, City)

#     def test_attributes(self):
#         """Test if city has all the required attributes"""
#         self.assertTrue(hasattr(self.city, 'state_id'))
#         self.assertTrue(hasattr(self.city, 'name'))

#     def test_default_values(self):
#         """Test if city attributes have default values"""
#         self.assertEqual(self.city.state_id, "")
#         self.assertEqual(self.city.name, "")

#     def test_save(self):
#         """Test if city can be saved to FileStorage"""
#         self.city.save()
#         self.assertIn(self.city.__class__.__name__ + '.' + self.city.id, FileStorage.all())

#     def test_to_dict(self):
#         """Test if city can be serialized to a dictionary"""
#         serialized = self.city.to_dict()
#         self.assertIsInstance(serialized, dict)
#         self.assertEqual(serialized['__class__'], 'City')
#         self.assertIsNotNone(serialized['id'])
#         self.assertIsNotNone(serialized['created_at'])
#         self.assertIsNotNone(serialized['updated_at'])

# if __name__ == '__main__':
#     unittest.main()
