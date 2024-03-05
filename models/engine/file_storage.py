#!/usr/bin/python3

import os
import uuid

class FileStorage:
    """A simple file storage system."""

    def __init__(self, base_dir):
        """Initialize the storage with a base directory."""
        self.base_dir = base_dir
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def save(self, file_name, data):
        """Save a file with the given data."""
        # Generate a unique file name
        unique_file_name = str(uuid.uuid4()) + '_' + file_name
        file_path = os.path.join(self.base_dir, unique_file_name)

        # Save the file
        with open(file_path, 'wb') as file:
            file.write(data)

        return unique_file_name

    def delete(self, file_name):
        """Delete a file by its name."""
        file_path = os.path.join(self.base_dir, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"No file named '{file_name}'")

    def exists(self, file_name):
        """Check if a file exists."""
        file_path = os.path.join(self.base_dir, file_name)
        return os.path.exists(file_path)

    def get_path(self, file_name):
        """Get the full path of a file."""
        return os.path.join(self.base_dir, file_name)

