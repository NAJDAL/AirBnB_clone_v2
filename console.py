#!/usr/bin/python3
"""Interactive console for managing objects of different classes."""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Contains functionality for the HBNB console."""

    # Prompt configuration for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax."""
        ...

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    # Additional commands
    def do_quit(self, command):
        """Exit the HBNB console."""
        exit()

    def help_quit(self):
        """Prints help documentation for quit."""
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """Handles EOF to exit program."""
        print()
        exit()

    def help_EOF(self):
        """Prints help documentation for EOF."""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Overrides the emptyline method of CMD."""
        pass

    # Methods for managing objects
    def do_create(self, args):
        """Create an object of any class."""
        ...

    def help_create(self):
        """Help information for the create method."""
        ...

    def do_show(self, args):
        """Show an individual object."""
        ...

    def help_show(self):
        """Help information for the show command."""
        ...

    def do_destroy(self, args):
        """Destroy a specified object."""
        ...

    def help_destroy(self):
        """Help information for the destroy command."""
        ...

    def do_all(self, args):
        """Show all objects, or all objects of a class."""
        ...

    def help_all(self):
        """Help information for the all command."""
        ...

    def do_count(self, args):
        """Count current number of class instances."""
        ...

    def help_count(self):
        """Help information for the count command."""
        ...

    def do_update(self, args):
        """Update a certain object with new info."""
        ...

    def help_update(self):
        """Help information for the update class."""
        ...

if __name__ == "__main__":
    HBNBCommand().cmdloop()
