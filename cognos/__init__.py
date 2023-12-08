import os
import sys
import asyncio
import json
from positioning import *
from notes import *
from tools import *
from artifact import *
import pathlib
import fnmatch

pathdict=[]
pathlib.path(".")  # This creates a new Path object representing the current directory (".").
filetype: str = "*.md"
# match any file with any extension in the current directory or any of its subdirectories, recursively.
for file in pathlib=pathlib.Path(".").glob(filetype):
    filename=str(file)
    pathdict.append(filename)

class FileTypeSelector:
    """
    a class that takes a directory in its constructor and has a method select_files(file_extension)
        that selects all files with a given extension in the directory or its subdirectories.
    """
    def __init__(self, directory="."):
        self.directory = directory

    def select_files(self, file_extension):
        """
        You can create a new FileTypeSelector and call `select_files("py")` to select all Python files
        :param file_extension:
        :return:
        """
        return pathlib.Path(self.directory).glob(f"**/*.{file_extension}")