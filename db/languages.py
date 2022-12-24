import os
import json
from typing import List
from models.language import Language

class Languages:

    parent_dir = os.getcwd()
    __file_path = f'{parent_dir}/languages.json'
    languages: List[Language] = []

    def __init__(self):
        pass

    def get(self) -> List[Language]:
        return self.languages

    def load(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                contents = file.read()
                self.languages = json.loads(contents)
        except Exception as e:
            return