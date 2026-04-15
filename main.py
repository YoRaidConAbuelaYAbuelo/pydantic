from storage.database import load_characters, save_characters
from models.character import Character
from models.item import Item

def add_character(name, strength, intelligence):
    chars = load_characters()
    new = Character(name=name, strength=strength, intelligence=intelligence)
    chars.append(new)
    save_characters(chars)
    return new

def add_item(character_name, item_name, quantity):
    chars = load_characters()
    for c in chars:
        if c.name == character_name:
            c.inventory.append(Item(name=item_name, quantity=quantity))
            save_characters(chars)
            return c
    raise ValueError("Character not found")