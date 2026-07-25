# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: HabitGarden
def demo_commands():
    """Компактный набор демо-команд для ручного тестирования HabitGarden."""
    import random
    from datetime import date, timedelta
    
    # Демо-привычки с разными параметрами
    habits = [
        {"name": "Пить воду", "streak": 5, "series": 3, "notes": "Начинаю с 2 стаканов"},
        {"name": "Чтение 15 мин", "streak": 0, "series": 1, "notes": ""},
        {"name": "Спорт", "streak": 12, "series": 4, "notes": "Утро или вечер"},
        {"name": "Медитация", "streak": 7, "series": 2, "notes": "5 минут достаточно"},
    ]
    
    # Генерация случайных напоминаний для каждой привычки
    reminders = []
    for h in habits:
        days_left = random.randint(1, 3)
        hour = random.choice([7, 8, 9])
        reminders.append({
            "habit": h["name"],
            "time": f"{hour}:00",
            "days_until": days_left
        })
    
    # Вывод демо-данных в формате таблицы (без markdown)
    print("=" * 45)
    print("DEMO: HabitGarden Test Data")
    print("=" * 45)
    print(f"{'Привычка':<20} {'Серия':>6} {'Стreak':>8}")
    print("-" * 34)
    for h in habits:
        print(f"{h['name']:<20} {h['series']:>6} {h['streak']:>8}")
    
    print()
    print("REMINDERS (next execution):")
    for r in reminders:
        print(f"  • {r['habit']} — через {r['days_until']} день(а) в {r['time']}")

demo_commands()
