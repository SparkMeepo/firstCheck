# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: HabitGarden
import json, os
from datetime import datetime

def load_profiles():
    path = "habit_garden_data/profiles.json"
    if not os.path.exists(path):
        return {"default": {"name": "Гость", "habits": {}, "notes": [], "streaks": {}}}
    with open(path) as f:
        return json.load(f)

def save_profiles(profiles):
    path = "habit_garden_data/profiles.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(profiles, f, indent=2)

def switch_profile(active_name):
    profiles = load_profiles()
    if active_name not in profiles and "default" in profiles:
        new_profile = {"name": active_name, "habits": {}, "notes": [], "streaks": {}}
        profiles[active_name] = new_profile
    elif active_name not in profiles:
        print(f"Профиль '{active_name}' не найден.")
        return False
    current = list(profiles.keys())[0] if len(profiles) == 1 else None
    for key, profile in profiles.items():
        if key != "default":
            current = key
            break
    active_profiles = {k: v for k, v in profiles.items() if k != "default"}
    if not active_profiles and len(profiles) > 1:
        active_profiles = {k: v for k, v in profiles.items()}
    profiles[current] = profiles[active_name]
    save_profiles(profiles)
    print(f"Переключен на профиль: {active_name}")
    return True

def get_active_profile():
    profiles = load_profiles()
    current = list(profiles.keys())[0] if len(profiles) == 1 else None
    for key, profile in profiles.items():
        if key != "default":
            current = key
            break
    return profiles.get(current, {})

def add_profile(name):
    profiles = load_profiles()
    if name not in profiles:
        new_profile = {"name": name, "habits": {}, "notes": [], "streaks": {}}
        profiles[name] = new_profile
        save_profiles(profiles)
        print(f"Профиль '{name}' создан.")
        return True
    else:
        print("Такой профиль уже существует.")
        return False

def list_profiles():
    profiles = load_profiles()
    if "default" in profiles:
        del profiles["default"]
    for name, data in profiles.items():
        print(f"{name}: {len(data['habits'])} привычек")
