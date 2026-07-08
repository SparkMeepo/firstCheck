# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: HabitGarden
def monthly_stats(self, month_year=None):
    if month_year is None:
        now = datetime.now()
        month_year = (now.month, now.year)
    
    year, month = month_year
    today = datetime(year, month, day=31).date()
    stats = {}
    for d in range(1, 29):
        dt = datetime(year, month, d)
        date_str = dt.strftime('%Y-%m-%d')
        if date_str not in self.habits: continue
        habit = self.habits[date_str]
        done_count = sum(1 for h in habit.history if h.done)
        stats[dt.date()] = {
            'habit': habit.name,
            'done': done_count,
            'total': len(habit.history),
            'streak_days': len([x for x in range(done_count)]),
        }
    return stats
