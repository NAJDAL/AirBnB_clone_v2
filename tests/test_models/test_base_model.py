#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import pycodestyle
import unittest
from datetime import datetime
from models.base_model import BaseModel
import inspect
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_pep8(self):
        """Test PEP-8 conformity."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstrings(self):
        """Test docstrings."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_methods(self):
        """Test if BaseModel has all required methods."""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """Test if BaseModel initializes correctly."""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_save(self):
        """Test save method of BaseModel."""
        base = BaseModel()
        created_at = base.created_at
        base.save()
        self.assertNotEqual(created_at, base.updated_at)

    def test_to_dict(self):
        """Test to_dict method of BaseModel."""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertIsInstance(base_dict["created_at"], str)
        self.assertIsInstance(base_dict["updated_at"], str)

    def test_uuid(self):
        """Test if the id of each BaseModel is unique."""
        base1 = BaseModel()
        base2 = BaseModel()
        base3 = BaseModel()
        ids = {base1.id, base2.id, base3.id}
        self.assertEqual(len(ids), 3)

    def test_str_method(self):
        """Test the __str__() method of BaseModel."""
        base = BaseModel()
        string_output = "[BaseModel] ({}) {}".format(base.id, base.__dict__)
        self.assertEqual(string_output, str(base))

    @classmethod
    def tearDownClass(cls):
        """Remove the file.json created after running the tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    @classmethod
    def setUpClass(cls):
        """Set up instances to be used in test cases."""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def tearDown(cls):
        """Remove the instance created after running each test."""
        del cls.base

    def test_class_attributes(self):
        """Test if the BaseModel instance has the correct attributes."""
        self.assertTrue(hasattr(self.base, "name"))
        self.assertTrue(hasattr(self.base, "num"))

    def test_instance_attributes(self):
        """Test if the BaseModel instance has the correct instance attributes."""
        self.assertEqual(self.base.name, "Kev")
        self.assertEqual(self.base.num, 20)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_created_and_updated_at(self):
        """Test the created_at and updated_at attributes."""
        base = BaseModel()
        created_at = base.created_at
        self.assertEqual(created_at, base.updated_at)
        base.save()
        self.assertNotEqual(created_at, base.updated_at)

    def test_dict_representation(self):
        """Test the dictionary representation of the BaseModel instance."""
        base_dict = self.base.to_dict()
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertIsInstance(base_dict["created_at"], str)
        self.assertIsInstance(base_dict["updated_at"], str)
        self.assertEqual(base_dict["name"], "Kev")
        self.assertEqual(base_dict["num"], 20)
