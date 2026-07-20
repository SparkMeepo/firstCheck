# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: HabitGarden
def check_overdue_reminders():
    now = datetime.now()
    overdue = []
    for reminder in reminders:
        if reminder["date"] < now and not reminder["done"]:
            overdue.append(reminder)
    print(f"Просрочено напоминаний: {len(overdue)}")
    return overdue
