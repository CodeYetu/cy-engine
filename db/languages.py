import os
import json
from typing import List
from models.language import Language

class Languages:

    """A class which represents a programming Language

    Thiis class mainly fetches the programming languages from the
    parent directory and deserialize it to a Language model.

    Note:
        Make sure you create a JSON file with all the programming
        languages at the root directory of this project.

    Attributes:
        parent_dir (str): Parent direcory
        __file_path (str): Path to the JSON file
        languages: A list containing the deserialized languages
    
    """

    parent_dir = os.getcwd()
    __file_path = f'{parent_dir}/languages.json'
    languages: List[Language] = []

    def __init__(self):
        pass

    def get(self) -> List[Language]:
        """Returns a list of languages from the class onject
        
        Returns:
            A list of languages
        
        """
        return self.languages

    def load(self) -> None:
        """Serializes the contents of the languages JSON file

        This method fetches and updates the languages attribute
        of the class with the contents of the languages.json file
        and desirealizes them to a list of languages.

        Note:
            if the file does not exist, then this method will just
            return and the languages attribute will be an empty list

        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                contents = file.read()
                self.languages = json.loads(contents)
        except Exception as e:
            if isinstance(e, FileNotFoundError):
                print(f'{self.__file_path} Not Found!')
            return