# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: HabitGarden
import json, os, random, datetime as dt

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки в структуру проекта."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект (dict).")
        
        # Инициализация отсутствующих полей с дефолтными значениями
        defaults = {
            "user_name": "",
            "habits": [],
            "series": {},
            "notes": {},
            "notifications": []
        }
        for key, default in defaults.items():
            if key not in data:
                data[key] = default
        
        # Проверка и нормализация списка привычек (добавление ID если нет)
        habits_list = data.get("habits", [])
        if isinstance(habits_list, list):
            for i, habit in enumerate(habits_list):
                if not isinstance(habit, dict):
                    raise ValueError(f"Пользовательская привычка {i} не является словарем.")
                if "id" not in habit:
                    habit["id"] = f"h_{len(data.get('habits', [])) + 1}"
        
        # Проверка структуры серий (series)
        series_data = data.get("series", {})
        if isinstance(series_data, dict):
            for habit_id, history in series_data.items():
                if not isinstance(history, list):
                    raise ValueError(f"История серии для привычки {habit_id} должна быть списком.")
        
        # Проверка заметок (notes)
        notes_data = data.get("notes", {})
        if isinstance(notes_data, dict):
            for habit_id, note_text in notes_data.items():
                if not isinstance(note_text, str):
                    raise ValueError(f"Заметка для привычки {habit_id} должна быть строкой.")
        
        # Проверка уведомлений (notifications)
        notifications_list = data.get("notifications", [])
        if isinstance(notifications_list, list):
            for notif in notifications_list:
                if not isinstance(notif, dict):
                    raise ValueError("Уведомление должно быть словарем.")
                required_keys = {"message", "enabled"}
                missing = [k for k in required_keys if k not in notif]
                if missing:
                    raise ValueError(f"В уведомлении не хватает полей: {missing}")
        
        # Сохранение загруженных данных в глобальную переменную проекта (если есть) или возврат
        global HABIT_GARDEN_DATA
        HABIT_GARDEN_DATA = data
        
        print(f"[HabitGarden] Начальные данные успешно загружены. Пользователь: {data.get('user_name', 'Гость')}")
        return data

    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка парсинга JSON: {e}") from e
