from typing import List
from db.languages import Languages

languages = Languages()
languages.load()
languages = languages.get()