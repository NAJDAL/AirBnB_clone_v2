#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
import pycodestyle
from models.city import City
from models.base_model import BaseModel
import os


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_pep8(self):
        """Test PEP-8 conformity."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/city.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstrings(self):
        """Test docstrings."""
        self.assertIsNotNone(City.__doc__)

    def test_subclass(self):
        """Test if City is a subclass of BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Test if City has the required attributes."""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

    def test_attribute_types(self):
        """Test attribute types of City."""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_save(self):
        """Test save method of City."""
        city = City()
        created_at = city.created_at
        city.save()
        self.assertNotEqual(created_at, city.updated_at)

    def test_to_dict(self):
        """Test to_dict method of City."""
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)

    @classmethod
    def tearDownClass(cls):
        """Remove the file.json created after running the tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
