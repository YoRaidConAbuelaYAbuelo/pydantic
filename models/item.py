from pydantic import BaseModel, validator

class Item(BaseModel):
    name: str
    quantity: int

    @validator("quantity")
    def quantity_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Quantity must be greater than 0.")
        return value