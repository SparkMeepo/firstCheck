# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: HabitGarden
class HabitTemplate:
    def __init__(self, title, description="", habit_type="daily", reminder_time=None):
        self.title = title
        self.description = description
        self.habit_type = habit_type
        self.reminder_time = reminder_time

    def create_record(self, user_id):
        return Record(
            user_id=user_id,
            title=self.title,
            description=self.description,
            habit_type=self.habit_type,
            reminder_time=self.reminder_time
        )
