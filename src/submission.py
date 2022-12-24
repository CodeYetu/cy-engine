from typing import Optional
from dataclasses import dataclass
"""Submission Model"""

@dataclass
class Submission:
    """A data class used to represent a Submission

    Attributes:
        id (int): A unique identifier for a code Submission
        language (str): The language which the code is written in
        code (str): The actual code to be executed
        stdin (str, optional): Standard input 
    
    """

    id: int
    language: str
    code: str
    stdin: Optional[str] = None