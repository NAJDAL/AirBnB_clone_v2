#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
import pycodestyle
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_pep8(self):
        """Test PEP-8 conformity."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/state.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_subclass(self):
        """Test if State is a subclass of BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """Test if State has the required attributes."""
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_attribute_types(self):
        """Test attribute types of State."""
        state = State()
        self.assertIsInstance(state.name, str)

    @classmethod
    def tearDownClass(cls):
        """Remove the file.json created after running the tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
