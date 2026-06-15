# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: HabitGarden
import json, uuid
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any

class Habit:
    def __init__(self, name: str, streak: int = 0):
        self.id = str(uuid.uuid4())
        self.name = name
        self.streak = streak
        self.completed_dates: List[str] = []
        self.notes: Dict[str, str] = {}

    def complete(self) -> bool:
        today = datetime.now().strftime("%Y-%m-%d")
        if not any(d == today for d in self.completed_dates):
            self.streak += 1
            self.completed_dates.append(today)
            return True
        return False

class HabitGardenApp:
    def __init__(self, data_file: str = "habits.json"):
        self.data_file = data_file
        self.habits: Dict[str, Habit] = {}
        self._load_data()

    def _load_data(self) -> None:
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            for name in raw_data.get('habits', []):
                self.habits[name] = Habit(name=name, streak=raw_data['habits'][name].get('streak', 0))
        except FileNotFoundError:
            pass

    def save(self) -> None:
        data = {"habits": {k: {"name": v.name, "streak": v.streak} for k, v in self.habits.items()}}
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_habit(self, name: str) -> Optional[Habit]:
        if name in self.habits:
            return None
        habit = Habit(name=name)
        self.habits[name] = habit
        self.save()
        return habit

# Демонстрационные данные и точка входа
if __name__ == "__main__":
    app = HabitGardenApp("habits.json")
    
    # Добавляем демо-привычки
    demo_habits = ["Пить воду", "Читать 10 минут", "Спорт"]
    for habit_name in demo_habits:
        app.add_habit(habit_name)

    print(f"Инициализирован HabitGarden с {len(app.habits)} привычками.")
    
    # Пример выполнения одной привычки
    if "Пить воду" in app.habits:
        success = app.habits["Пить воду"].complete()
        print(f"Статус 'Пить вода': {'Выполнено' if success else 'Уже выполнено сегодня'} (Серия: {app.habits['Пить вода'].streak})")
