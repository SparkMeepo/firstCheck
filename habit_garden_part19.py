# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: HabitGarden
def archive_habits(habit, days_back=30):
    """Archive habit if it hasn't been recorded in the last N days."""
    now = datetime.now()
    last_record = max(habit.get("last_streak_date", now), default=now)
    if (now - last_record).days > days_back:
        archived, _ = HabitGarden.habits.insert_one(
            {**habit, "status": "archived"}
        )
        return archived
