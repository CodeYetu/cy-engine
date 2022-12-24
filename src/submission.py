from typing import Optional
from dataclasses import dataclass

@dataclass
class Submission:
    id: int
    language: str
    code: str
    stdin: Optional[str] = None