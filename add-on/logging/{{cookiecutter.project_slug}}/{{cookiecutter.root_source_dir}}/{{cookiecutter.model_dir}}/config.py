from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class Config:
    environment: str
    logging: Dict[str,Any]
