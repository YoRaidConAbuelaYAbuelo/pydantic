from pathlib import Path
import json
from typing import List
from models.character import Character

DB_FILE = Path("storage/database.json")

def load_characters() -> List[Character]:
    if not DB_FILE.exists() or DB_FILE.stat().st_size == 0:
        return [] 
    try:
        with DB_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return [Character(**c) for c in data]
    except (json.JSONDecodeError, ValueError, TypeError):
        return []

def save_characters(characters: List[Character]):
    DB_FILE.parent.mkdir(exist_ok=True)
    with DB_FILE.open("w", encoding="utf-8") as f:
        json.dump([c.model_dump() for c in characters], f, indent=4)