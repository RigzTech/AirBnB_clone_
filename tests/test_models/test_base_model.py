#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
# storage = __import__('models.engine.file_storage').FileStorage
import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """test case for the BaseModel class"""

    def setUp(self):
        """setup for the test case"""
        self.base_model = BaseModel()

    def tearDown(self):
        """teardown for the test case"""
        FileStorage._FileStorage__objects = {}

    def test_is_an_instance(self):
        """Test if base_model is an instance of BaseModel"""
        self.assertIsInstance(self.base_model, BaseModel)

    def test_has_all_attributes(self):
        """Test if base_model has all the required attributes"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_has_default_values(self):
        """Test if base_model attributes have default values"""
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)

    def test_to_dict(self):
        """Test if base_model can be serialized to a dictionary"""
        serialized = self.base_model.to_dict()
        self.assertIsInstance(serialized, dict)
        self.assertEqual(serialized['__class__'], 'BaseModel')
        self.assertIsNotNone(serialized['created_at'])
        self.assertIsNotNone(serialized['updated_at'])
        self.assertIsNotNone(serialized['id'])

    # def test_save_fun(self):
    #     """Test if base_model can be saved to FileStorage"""
    #     self.base_model.save()
    #     self.assertIn(
    #         self.base_model.__class__.__name__ + '.' + self.base_model.id,
    #         FileStorage.all()
    #         # storage = FileStorage()
    #         # storage.all()
    #     )


if __name__ == '__main__':
    unittest.main()
