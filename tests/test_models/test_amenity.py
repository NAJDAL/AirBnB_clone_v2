#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import pycodestyle
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from os import getenv
from time import sleep
from unittest.mock import patch


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_is_subclass(self):
        """Test if Amenity is a subclass of BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Test the attributes of Amenity."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertIsInstance(amenity.name, str)
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        """Test the to_dict() method of Amenity."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)

    def test_str(self):
        """Test the __str__() method of Amenity."""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))

    def test_name_attr(self):
        """Test the name attribute of Amenity."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertIsNone(amenity.name)
        else:
            self.assertEqual(amenity.name, "")

    def test_save_method(self):
        """Test the save() method of Amenity."""
        amenity = Amenity()
        created_at = amenity.created_at
        sleep(0.1)
        amenity.save()
        self.assertLess(created_at, amenity.updated_at)

    def test_id_unique(self):
        """Test if the id of each Amenity is unique."""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_instance(self):
        """Test if Amenity inherits from BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_created_at(self):
        """Test the created_at attribute of Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_updated_at(self):
        """Test the updated_at attribute of Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_has_methods(self):
        """Test if Amenity has all methods from BaseModel."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "__init__"))
        self.assertTrue(hasattr(amenity, "to_dict"))
        self.assertTrue(hasattr(amenity, "save"))

    def test_user_id_and_createat(self):
        """Test the id and created_at attributes for Amenity."""
        amenity1 = Amenity()
        sleep(0.1)
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_pep8(self):
        """Test for PEP-8."""
        pep8 = pycodestyle.StyleGuide(quiet=True)
        result = pep8.check_files(["models/amenity.py"])
        self.assertEqual(result.total_errors, 0, "PEP-8 style issues found")
