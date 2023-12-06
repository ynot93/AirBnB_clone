"""
This module creates a storage object which loads data from
the file that it is stored in.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
