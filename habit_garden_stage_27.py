# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: HabitGarden
def reset_demo_data():
    """Сбросить все демо-данные: привычки, серии, заметки, напоминания."""
    habits = []
    series = {}
    notes = []
    reminders = []
    for h in demo_habits:
        habits.append(Habit(h.name, streak=0))
        series[h.name] = Series()
    return habits, series, notes, reminders

def clear_state():
    """Очистить текущее состояние приложения."""
    global habits, series, notes, reminders
    habits, series, notes, reminders = reset_demo_data()
