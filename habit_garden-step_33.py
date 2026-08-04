# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: HabitGarden
class HabitEntry:
    def __init__(self, name="", description="", streak=0, notes=""):
        self.name = name
        self.description = description
        self.streak = 0
        self.notes = ""

    def do(self):
        """Отметить привычку как выполненную."""
        self.streak += 1
        return True

    def undo(self):
        """Откат последнего действия: вернуть streak на предыдущее значение и стереть заметку."""
        if self.streak > 0:
            # Сохраняем текущее состояние перед откатом, чтобы можно было отменить отмену (опционально)
            previous_streak = self.streak - 1
            previous_notes = self.notes
            self.streak = previous_streak
            self.notes = ""
        return True

    def get_status(self):
        """Возвращает текущий статус привычки."""
        status = {
            "name": self.name,
            "description": self.description,
            "streak": self.streak,
            "notes": self.notes
        }
        return status

    def set_notes(self, notes):
        """Установить заметку для привычки."""
        self.notes = notes
