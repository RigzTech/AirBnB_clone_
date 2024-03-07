# #!/usr/bin/python3

# import unittest
# from models.place import Place
# from models.engine.file_storage import FileStorage

# class TestPlace(unittest.TestCase):
#     """Defines the test case for the Place class"""

#     def setUp(self):
#         """Defines the setup for the test case"""
#         self.place = Place()

#     def tearDown(self):
#         """Defines the teardown for the test case"""
#         FileStorage._FileStorage__objects = {}

#     def test_instance(self):
#         """Test if place is an instance of Place"""
#         self.assertIsInstance(self.place, Place)

#     def test_attributes(self):
#         """Test if place has all the required attributes"""
#         self.assertTrue(hasattr(self.place, 'city_id'))
#         self.assertTrue(hasattr(self.place, 'user_id'))
#         self.assertTrue(hasattr(self.place, 'name'))
#         self.assertTrue(hasattr(self.place, 'description'))
#         self.assertTrue(hasattr(self.place, 'number_rooms'))
#         self.assertTrue(hasattr(self.place, 'number_bathrooms'))
#         self.assertTrue(hasattr(self.place, 'max_guest'))
#         self.assertTrue(hasattr(self.place, 'price_by_night'))
#         self.assertTrue(hasattr(self.place, 'latitude'))
#         self.assertTrue(hasattr(self.place, 'longitude'))
#         self.assertTrue(hasattr(self.place, 'amenity_ids'))

#     def test_default_values(self):
#         """Test if place attributes have default values"""
#         self.assertEqual(self.place.city_id, "")
#         self.assertEqual(self.place.user_id, "")
#         self.assertEqual(self.place.name, "")
#         self.assertEqual(self.place.description, "")
#         self.assertEqual(self.place.number_rooms, 0)
#         self.assertEqual(self.place.number_bathrooms, 0)
#         self.assertEqual(self.place.max_guest, 0)
#         self.assertEqual(self.place.price_by_night, 0)
#         self.assertEqual(self.place.latitude, 0.0)
#         self.assertEqual(self.place.longitude, 0.0)
#         self.assertEqual(self.place.amenity_ids, [])

#     def test_save(self):
#         """Test if place can be saved to FileStorage"""
#         self.place.save()
#         self.assertIn(self.place.__class__.__name__ + '.' + self.place.id, FileStorage.all())

#     def test_to_dict(self):
#         """Test if place can be serialized to a dictionary"""
#         serialized = self.place.to_dict()
#         self.assertIsInstance(serialized, dict)
#         self.assertEqual(serialized['__class__'], 'Place')
#         self.assertIsNotNone(serialized['id'])
#         self.assertIsNotNone(serialized['created_at'])
#         self.assertIsNotNone(serialized['updated_at'])

# if __name__ == '__main__':
#     unittest.main()
