from pydantic import BaseModel, validator

class Spell(BaseModel):
    name: str
    mana_cost: int

    @validator("mana_cost")
    def mana_cost_cannot_be_negative(cls, value):
        if value < 0:
            raise ValueError("Mana cost cannot be negative.")
        return value