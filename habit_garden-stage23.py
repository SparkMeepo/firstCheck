# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: HabitGarden
def print_habit_table(self):
    """Выводит таблицу прогресса привычек в консоль."""
    width = 20
    sep = '-' * (width + len('|'))
    print(sep)
    print(f'| {"Название":{width}} | Прогресс | Серия | Заметка |')
    print(sep)
    for h in self.habits:
        streak_str = str(h.streak) if h.streak else '0'
        note_short = (h.note or '')[:12] + '..' if len(h.note or '') > 14 else (h.note or '')
        print(f'| {str(h.name).ljust(width)} | {streak_str:>3}   | {note_short} |')
    print(sep)
