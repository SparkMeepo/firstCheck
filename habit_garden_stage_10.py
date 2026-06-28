# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: HabitGarden
def export_state_to_json():
    import json
    from datetime import datetime
    
    # Формируем словарь состояния приложения
    state = {
        "app_name": "HabitGarden",
        "export_timestamp": datetime.now().isoformat(),
        "habits": habits,  # Предполагается, что 'habits' — это глобальный список объектов привычек
        "settings": settings if locals().get('settings') else {},  # Опциональные настройки
        "user_notes": user_notes if locals().get('user_notes') else {}  # Заметки пользователя
    }
    
    # Преобразуем объекты привычек в простые словари для JSON-сериализации
    serializable_habits = []
    for habit in state["habits"]:
        habit_dict = {
            "id": getattr(habit, 'id', None),
            "name": getattr(habit, 'name', ''),
            "streak_count": getattr(habit, 'streak_count', 0),
            "created_at": getattr(habit, 'created_at', '').isoformat() if hasattr(getattr(habit, 'created_at', None), 'isoformat') else str(getattr(habit, 'created_at', '')),
            "is_active": getattr(habit, 'is_active', True)
        }
        serializable_habits.append(habit_dict)
    
    state["habits"] = serializable_habits
    
    # Сериализуем состояние в строку JSON с отступом для читаемости
    json_string = json.dumps(state, indent=2, ensure_ascii=False)
    
    return json_string

# Пример вызова (раскомментируйте при необходимости):
# print(export_state_to_json())
