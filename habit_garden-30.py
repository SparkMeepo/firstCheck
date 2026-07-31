# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: HabitGarden
import json, os
from datetime import date

USER_DATA = "user_data.json"

def save_user_profile(user_id, habits):
    with open(USER_DATA, 'w') as f:
        json.dump({user_id: {"habits": habits}}, f)

def load_user_profile(user_id):
    if not os.path.exists(USER_DATA):
        return {}
    try:
        with open(USER_DATA, 'r') as f:
            data = json.load(f)
        return data.get(user_id, {})
    except (json.JSONDecodeError, IOError):
        return {}

def switch_user(user_id=None):
    if user_id is None and os.path.exists(USER_DATA):
        with open(USER_DATA, 'r') as f:
            data = json.load(f)
        user_id = list(data.keys())[0] if len(data) == 1 else input("Select user ID: ")
    return user_id
