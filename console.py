#!/usr/bin/python3

import cmd
import json
import uuid
from datetime import datetime
from models import User, State, City, Place, Review
from engine.file_storage import FileStorage

# Initialize FileStorage
storage = FileStorage('./storage')

class AirBnBShell(cmd.Cmd):
    """A command interpreter for managing AirBnB objects."""

    prompt = '(AirBnB) '

    def do_create(self, arg):
        """Create a new object (e.g., User, Place)."""
        args = arg.split()
        if len(args) < 2:
            print("Usage: create <object_type> <attribute1=value1> <attribute2=value2> ...")
            return

        obj_type = args[0]
        attributes = dict(item.split('=') for item in args[1:])

        if obj_type == 'User':
            user = User(**attributes)
            user.save()
            print(f"Created User: {user.id}")
        elif obj_type == 'Place':
            place = Place(**attributes)
            place.save()
            print(f"Created Place: {place.id}")
        # Add more object types as needed
        else:
            print(f"Unsupported object type: {obj_type}")

    def do_show(self, arg):
        """Show an object's details."""
        args = arg.split()
        if len(args) != 2:
            print("Usage: show <object_type> <id>")
            return

        obj_type, obj_id = args
        if obj_type == 'User':
            user = User.find(obj_id)
            if user:
                print(user.to_dict())
            else:
                print("User not found.")
        elif obj_type == 'Place':
            place = Place.find(obj_id)
            if place:
                print(place.to_dict())
            else:
                print("Place not found.")
        # Add more object types as needed
        else:
            print(f"Unsupported object type: {obj_type}")

    def do_delete(self, arg):
        """Delete an object."""
        args = arg.split()
        if len(args) != 2:
            print("Usage: delete <object_type> <id>")
            return

        obj_type, obj_id = args
        if obj_type == 'User':
            user = User.find(obj_id)
            if user:
                user.delete()
                print("User deleted.")
            else:
                print("User not found.")
        elif obj_type == 'Place':
            place = Place.find(obj_id)
            if place:
                place.delete()
                print("Place deleted.")
            else:
                print("Place not found.")
        # Add more object types as needed
        else:
            print(f"Unsupported object type: {obj_type}")

    def do_EOF(self, line):
        """Exit the command interpreter."""
        return True

if __name__ == '__main__':
    AirBnBShell().cmdloop()
