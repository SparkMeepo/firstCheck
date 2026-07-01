# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: HabitGarden
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict) and 'habits' in data:
            return data['habits']
        elif isinstance(data, list):
            return data
        else:
            print("Ошибка: Неправильный формат данных в JSON.")
            return []
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON: {e}")
        return []
