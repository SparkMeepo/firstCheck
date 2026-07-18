# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: HabitGarden
class Reminder:
    def __init__(self, habit_id, reminder_date, note=""):
        self.habit_id = habit_id
        self.reminder_date = reminder_date  # str date like "2024-12-31"
        self.note = note

    def is_due(self):
        return datetime.date.today() >= datetime.date.fromisoformat(self.reminder_date)
