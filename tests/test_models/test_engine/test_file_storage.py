import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.base_model = BaseModel()
        self.base_model.name = "My_First_Model"
        self.base_model.my_number = 89
        self.storage.new(self.base_model)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_fun(self):
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn(f"BaseModel.{self.base_model.id}", all_objs)

    def test_new_fun(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objs = self.storage.all()
        self.assertIn(f"BaseModel.{new_model.id}", all_objs)
        self.assertEqual(len(all_objs), 2)

    def test_save_fun(self):
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_fun(self):
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn(f"BaseModel.{self.base_model.id}", all_objs)


if __name__ == '__main__':
    unittest.main()
