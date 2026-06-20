# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: HabitGarden
def edit_habit(habit_id: str, updates: dict) -> HabitRecord | None:
    """Редактирует запись по ID, возвращая обновлённый объект или None."""
    for i, habit in enumerate(HABIT_RECORDS):
        if habit.id == habit_id:
            HABIT_RECORDS[i] = HabitRecord(
                id=habit.id, name=updates.get("name", habit.name), streak=updates.get("streak", habit.streak),
                notes=updates.get("notes", habit.notes) or "", reminders=updates.get("reminders", habit.reminders) or []
            )
            print(f"Запись #{habit_id} обновлена.")
            return HABIT_RECORDS[i]
    print(f"Запись с ID {habit_id} не найдена для редактирования.")
    return None
