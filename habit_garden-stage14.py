# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: HabitGarden
def generate_summary(habits, completed_today):
    """Генерирует краткую текстовую сводку состояния приложения."""
    lines = ["=== Сводка HabitGarden ==="]
    
    if not habits:
        lines.append("Привычек пока нет.")
    else:
        total_habits = len(habits)
        completed_count = sum(1 for h in habits if h.get('completed_today'))
        
        lines.append(f"Всего привычек: {total_habits}")
        lines.append(f"Выполнено сегодня: {completed_count}/{total_habits}")
        
        streaks = [h['streak'] for h in habits]
        if streaks:
            max_streak = max(streaks)
            avg_streak = sum(streaks) / len(streaks)
            lines.append(f"Максимальная серия: {max_streak} дней")
            lines.append(f"Средняя серия: {avg_streak:.1f} дня")
        
        notes_count = sum(1 for h in habits if h.get('notes'))
        if notes_count > 0:
            lines.append(f"Заметок добавлено: {notes_count}")
    
    today_date = completed_today.strftime("%d.%m.%Y") if hasattr(completed_today, 'strftime') else str(completed_today)
    lines.append(f"Дата отчёта: {today_date}")
    
    return "\n".join(lines)
