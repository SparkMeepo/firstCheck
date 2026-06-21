# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: HabitGarden
def delete_habit(habit_id: int) -> None:
    if not isinstance(habit_id, int):
        raise ValueError("habit_id должен быть целым числом")
    try:
        habits.remove(habit_id)
        print(f"Привычка {habit_id} удалена.")
    except (IndexError, ValueError):
        print(f"Привычка с id={habit_id} не найдена или уже отсутствует в списке.")

def delete_note(note_id: int) -> None:
    if not isinstance(note_id, int):
        raise ValueError("note_id должен быть целым числом")
    try:
        notes.remove(note_id)
        print(f"Заметка {note_id} удалена.")
    except (IndexError, ValueError):
        print(f"Заметка с id={note_id} не найдена или уже отсутствует в списке.")

def delete_series(series_id: int) -> None:
    if not isinstance(series_id, int):
        raise ValueError("series_id должен быть целым числом")
    try:
        series.remove(series_id)
        print(f"Серия {series_id} удалена.")
    except (IndexError, ValueError):
        print(f"Серия с id={series_id} не найдена или уже отсутствует в списке.")

def delete_reminder(reminder_id: int) -> None:
    if not isinstance(reminder_id, int):
        raise ValueError("reminder_id должен быть целым числом")
    try:
        reminders.remove(reminder_id)
        print(f"Напоминание {reminder_id} удалено.")
    except (IndexError, ValueError):
        print(f"Напоминание с id={reminder_id} не найдено или уже отсутствует в списке.")
