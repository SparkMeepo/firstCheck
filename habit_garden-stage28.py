# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: HabitGarden
def print_stats(self):
        """Print key project metrics."""
        habits = self.get_habits()
        notes = self.get_notes()
        reminders = self.get_reminders()
        series = []
        for h in habits:
            if h["series"]:
                series.append(h["series"])

        print("\n=== HabitGarden Stats ===")
        total = len(habits) + len(notes) + len(reminders) + len(series)
        print(f"Total items tracked: {total}")
        print(f"Habits: {len(habits)}")
        if habits:
            active = sum(1 for h in habits if self.check_habit(h))
            streaks = [h["series"][-1] if h.get("series") and h["series"] else 0 for h in habits]
            avg_streak = (sum(streaks) / len(streaks)) if total > 0 else 0
            print(f"Active today: {active}/{total}")
            print(f"Avg streak: {avg_streak:.1f} days")

        if notes:
            print(f"Notes: {len(notes)}")
        if reminders:
            print(f"Reminders: {len(reminders)}")

        for s in series:
            print(f"Series '{s[0]}': {s[1]} consecutive days")
