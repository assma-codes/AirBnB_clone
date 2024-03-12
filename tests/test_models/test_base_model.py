#!/usr/bin/python3
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
import os

class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""
    def test_init(self):
        my_models = BaseModel()
        self.assertIsNotNone(my_models.id)
        self.assertIsNotNone(my_models.created_at)
        self.assertIsNotNone(my_models.updated_at)


    def test_to_dict(self):
        my_models = BaseModel()
        my_models_dict = my_models.to_dict()
        self.assertEqual(my_models_dict,dict)
        self.assertEqual(my_models_dict["__class__"],"BaseModel")
        self.assertEqual(my_models_dict['id'],my_models.id)
        self.assertEqual(my_models_dict["created_at"],my_models.created_at.isoformat())
        self.assertEqual(my_models_dict["updated_at"],my_models.updated_at.isoformat())
    def test_str(self):
        my_model = BaseModel()
        my_models = str(my_model)
        self.assertTrue(my_models.startswith("BaseModel"))
        self.assertIn(my_model.id,my_models)
        self.assertIn(my_model.__dict__,my_models)
    
    def test_two_models_unique_ids(self):
        un_id1 = BaseModel()
        un_id2 = BaseModel()
        self.assertNotEqual(un_id1.id, un_id2.id)
    
    def test_two_models_different_created_at(self):
        created_at1 = BaseModel()
        sleep(0.05)
        created_at2 = BaseModel()
        self.assertLess(created_at1.created_at, created_at2.created_at)

    def test_two_models_different_created_at(self):
        updated_at1 = BaseModel()
        sleep(0.05)
        updated_at2 = BaseModel()
        self.assertLess(updated_at1.updated_at(), updated_at2.updated_at)   
    
    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

class TestBaseModel_save(unittest.TestCase):
    @classmethod
    def set_Up(self):
        try:
            os.rename("file.json", "tmpl")
        except IOError:
            pass

    @classmethod
    def tear_Down(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmpl", "file.json")
        except IOError:
            pass
    def test_save(self):
        my_models = BaseModel()
        init_updated_at = my_models.updated_at
        current_updated_at = my_models.save()
        self.assertNotEqual(init_updated_at,current_updated_at)   
    

    def test_one_save(self):
        my_models = BaseModel()
        sleep(0.05)
        first_updated_at = my_models.updated_at
        my_models.save()
        self.assertLess(first_updated_at, my_models.updated_at)

    def test_two_saves(self):
        my_models = BaseModel()
        sleep(0.05)
        first_updated_at = my_models.updated_at
        my_models.save()
        second_updated_at = my_models.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        my_models.save()
        self.assertLess(second_updated_at, bm.updated_at)
    
    def test_save_updates_files(self):
        my_models = BaseModel()
        my_models.save()
        my_models_id = "BaseModel." + my_models.id
        with open("file.json", "r") as f:
            self.assertIn(my_models_id, f.read())


    def test_save_with_arg(self):
        my_models = BaseModel()
        with self.assertRaises(TypeError):
            my_models.save(None)



if __name__ == '__main__':
    unittest.main()