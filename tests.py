import unittest
from unittest.mock import mock_open, patch
import json

from models.character import Character
from models.item import Item
from models.spell import Spell
from storage.database import save_characters, load_characters
from main import add_character, add_item

class TestModels(unittest.TestCase):

    def test_character_valid(self):
        char = Character(name="Aragon", strength=10, intelligence=12)
        self.assertEqual(char.name, "Aragon")
        self.assertEqual(char.strength, 10)

    def test_item_valid(self):
        item = Item(name="Sword", quantity=3)
        self.assertEqual(item.quantity, 3)

    def test_spell_valid(self):
        spell = Spell(name="Fireball", mana_cost=5)
        self.assertEqual(spell.mana_cost, 5)

class TestValidation(unittest.TestCase):

    def test_character_invalid_stat(self):
        with self.assertRaises(ValueError):
            Character(name="Bad", strength=50, intelligence=10)

    def test_item_invalid_quantity(self):
        with self.assertRaises(ValueError):
            Item(name="Broken", quantity=0)

    def test_spell_invalid_mana(self):
        with self.assertRaises(ValueError):
            Spell(name="Dark Magic", mana_cost=-1)

class TestCRUD(unittest.TestCase):

    def test_add_character_increases_list(self):
        mock_list = []

        with patch("builtins.open", mock_open()):
            with patch("main.load_characters", return_value=mock_list):
                new_char = add_character("Legolas", 15, 14)
                self.assertEqual(len(mock_list), 1)
                self.assertEqual(mock_list[0].name, "Legolas")

    def test_add_item_to_character(self):
        char = Character(name="Legolas", strength=18, intelligence=8)
        mock_list = [char]

        with patch("builtins.open", mock_open()):
            with patch("main.load_characters", return_value=mock_list):
                updated = add_item("Legolas", "Axe", 2)
                self.assertEqual(len(updated.inventory), 1)
                self.assertEqual(updated.inventory[0].name, "Axe")


if __name__ == "__main__":
    unittest.main()