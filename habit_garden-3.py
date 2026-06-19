# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: HabitGarden
import json
from datetime import datetime, timedelta
from typing import Optional

class HabitRecord:
    def __init__(self, habit_name: str, completed: bool = False, note: Optional[str] = None):
        self.habit_name = habit_name
        self.completed = completed
        self.note = note
        self.timestamp = datetime.now()

    def to_dict(self) -> dict:
        return {
            "habit_name": self.habit_name,
            "completed": self.completed,
            "note": self.note,
            "timestamp": self.timestamp.isoformat()
        }

class HabitGardenState:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.records = []
            cls._instance.save_to_memory()
        return cls._instance

    @classmethod
    def reset(cls):
        cls._instance = None

    def save_to_memory(self):
        with open("habits.json", "w") as f:
            json.dump([r.to_dict() for r in self.records], f)

    def add_record(self, habit_name: str, completed: bool = False, note: Optional[str] = None) -> HabitRecord:
        record = HabitRecord(habit_name, completed, note)
        self.records.append(record)
        self.save_to_memory()
        return record

    def get_records(self) -> list:
        return [r.to_dict() for r in self.records]
