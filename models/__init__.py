#!/usr/bin/python3
"""
initialize the models package
"""

from . import engine

storage = engine.file_storage.FileStorage()
storage.reload()
