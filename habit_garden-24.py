# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: HabitGarden
def print_habit_entry(entry):
    """Компактный вывод одной записи с деталями."""
    if not entry:
        return "Нет записей."
    parts = [f"🌱 {entry.get('name', 'Без имени')}", f"Статус: {'✅' if entry.get('done') else '❌'}"]
    for key in ['streak', 'series', 'notes']:
        val = entry.get(key)
        if val is not None:
            parts.append(f"{key.capitalize()}: {val}")
    print('\n'.join(parts))

print_habit_entry({
    "name": "Чтение 30 мин",
    "done": True,
    "streak": 5,
    "series": [True, False, True],
    "notes": "Книга 'Атомные привычки'"
})
