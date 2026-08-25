# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: HabitGarden
def get_next_action(habit, streak, notes, reminders, goals):
    if not habit:
        return "Нет привычек — начни с одной маленькой цели."
    if streak < 3:
        return f"Продолжай делать {habit['name']} — серия пока слабая ({streak} раз), не сдавайся!"
    if streak >= 7:
        return f"🎉 Отлично! Ты уже {streak} дней подряд делаешь {habit['name']}! Попробуй увеличить цель или добавить новую привычку."
    if habit.get("notes") and "заметка" in habit["notes"].lower():
        return f"Отличный прогресс с {habit['name']}! {habit['notes']}"
    if reminders:
        return f"Не забудь напоминания: {reminders}"
    if goals:
        return f"Двигаешься к цели {goals}: {habit['name']} — серия {streak}"
    return "Все выглядит хорошо — продолжай в том же духе и добавь новые привычки, когда будешь готов!"
