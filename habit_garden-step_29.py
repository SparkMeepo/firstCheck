# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: HabitGarden
import json, os

def load_config():
    config_path = "habitgarden/config.json"
    if not os.path.exists(config_path):
        return {
            "theme": {"bg": "#1a1a2e", "fg": "#eee", "accent": "#0f3460"},
            "language": "ru",
            "notifications_enabled": True,
            "daily_reminder_hour": 9,
            "default_streak_goal": 7,
        }
    with open(config_path) as f:
        return json.load(f)

def save_config(cfg):
    path = "habitgarden/config.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(cfg, f, indent=2)
