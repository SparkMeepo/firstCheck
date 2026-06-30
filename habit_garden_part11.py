# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: HabitGarden
import json, os
DATA_FILE = "habits.json"
def save_data(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[ERROR] Не удалось сохранить данные в {DATA_FILE}: {e}")
        return False

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"habits": [], "settings": {"notifications_enabled": False}}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Восстанавливаем структуру по умолчанию, если файл поврежден или устарел
        if not isinstance(data, dict):
            return {"habits": [], "settings": {"notifications_enabled": False}}
        default_settings = {"notifications_enabled": False}
        for key in ["habits", "streaks", "notes"]:
            if key not in data:
                data[key] = []
        if "settings" not in data or not isinstance(data["settings"], dict):
            data["settings"] = default_settings.copy()
        else:
            for k, v in default_settings.items():
                if k not in data["settings"]:
                    data["settings"][k] = v
        return data
    except Exception as e:
        print(f"[ERROR] Ошибка чтения файла {DATA_FILE}: {e}")
        return {"habits": [], "streaks": {}, "notes": {}, "settings": default_settings}

# Пример использования в конце программы
if __name__ == "__main__":
    current_data = load_data()
    # Добавьте ваши данные сюда перед сохранением, например:
    # current_data["habits"].append({"id": 1, "title": "Новая привычка", "completed": False})
    save_data(current_data)
