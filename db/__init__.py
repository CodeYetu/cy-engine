"""
    This module acts as a stub for fetching static data.
    By default the module will return an instance of languages

    Classes:
        Languages
"""

from typing import List
from db.languages import Languages

languages = Languages()
languages.load()