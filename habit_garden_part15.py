# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: HabitGarden
def weekly_stats(self, date):
    """Расчёт недельной статистики по датам."""
    stats = {}
    for day in range(7):
        d = date + timedelta(days=day)
        weekday = d.weekday()
        if weekday not in stats:
            stats[weekday] = {"count": 0, "days_done": [], "note_count": 0}
        done = self.get_habits_for_date(d)
        for h in done:
            stats[weekday]["count"] += 1
            stats[weekday]["days_done"].append(h.id if hasattr(h, 'id') else str(h))
        notes = self.get_notes_for_date(d)
        stats[weekday]["note_count"] = len(notes)
    return stats
