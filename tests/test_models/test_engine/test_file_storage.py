#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_arg(self):
        my_model = FileStorage()
        type_my_model = type(FileStorage())
        self.assertEqual(type_my_model , my_model )

    def test_FileStorage_instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_string(self):
        type_my_model = type(FileStorage.__file_path)

        self.assertEqual(str,type_my_model )
       
    def testFileStorage_objects_is_private_dicts(self):
        type_my_model = type(FileStorage.__objects)
        self.assertEqual(dict, type_my_model )

    def test_storage_initializes_model(self):
        type_my_model = type(models.storage)
        self.assertEqual(type_my_model, FileStorage)
class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

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
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        all_test = type(models.storage.all())
        self.assertEqual(dict, all_test)

    def test_all_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        b_m = BaseModel()
        u_s = User()
        s_t = State()
        p_l = Place()
        c_y = City()
        a_m = Amenity()
        r_v = Review()
        models.storage.new(b_m)
        models.storage.new(u_s)
        models.storage.new(s_t)
        models.storage.new(p_l)
        models.storage.new(c_y)
        models.storage.new(a_m)
        models.storage.new(r_v)
        my_models_kays = models.storage.all().keys()
        my_models_values = models.storage.all().values()
        self.assertIn("BaseModel." + b_m.id, )
        self.assertIn(b_m,my_models_values )
        self.assertIn("User." + u_s.id, my_models_kays)
        self.assertIn(u_s, my_models_values)
        self.assertIn("State." + s_t.id, my_models_kays)
        self.assertIn(s_t, my_models_values)
        self.assertIn("Place." + p_l.id, my_models_kays)
        self.assertIn(p_l, my_models_values)
        self.assertIn("City." + c_y.id, my_models_kays)
        self.assertIn(c_y, my_models_values)
        self.assertIn("Amenity." + a_m.id, my_models_kays)
        self.assertIn(a_m, my_models_values)
        self.assertIn("Review." + r_v.id, my_models_kays)
        self.assertIn(r_v, my_models_values)

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        b_m = BaseModel()
        u_s = User()
        s_t = State()
        p_l = Place()
        c_y = City()
        a_m = Amenity()
        r_v = Review()
        models.storage.new(b_m)
        models.storage.new(u_s)
        models.storage.new(s_t)
        models.storage.new(p_l)
        models.storage.new(c_y)
        models.storage.new(a_m)
        models.storage.new(r_v)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + b_m.id, save_text)
            self.assertIn("User." + u_s.id, save_text)
            self.assertIn("State." + s_t.id, save_text)
            self.assertIn("Place." + p_l.id, save_text)
            self.assertIn("City." + c_y.id, save_text)
            self.assertIn("Amenity." + a_m.id, save_text)
            self.assertIn("Review." + r_v.id, save_text)
