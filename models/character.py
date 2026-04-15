from pydantic import BaseModel, validator
from typing import List
from .item import Item
from .spell import Spell

class Character(BaseModel):
    name: str
    strength: int
    intelligence: int
    inventory: List[Item] = []
    spells: List[Spell] = []

    @validator("strength", "intelligence")
    def stats_between_1_and_20(cls, value):
        if not 1 <= value <= 20:
            raise ValueError("Stats must be between 1 and 20.")
        return value