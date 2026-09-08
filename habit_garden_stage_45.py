# === Stage 45: Добавь восстановление из резервной копии ===
# Project: HabitGarden
import json, datetime

def restore_backup(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✅ Резервная копия из {filename} успешно восстановлена.")
        return data
    except FileNotFoundError:
        print(f"❌ Файл резервной копии не найден: {filename}")
        return None
    except json.JSONDecodeError:
        print(f"❌ Файл резервной копии повреждён: {filename}")
        return None

if __name__ == "__main__":
    backup_file = "habitgarden_backup.json"
    backup = restore_backup(backup_file)
    if backup:
        with open("habitgarden.json", "w", encoding='utf-8') as f:
            json.dump(backup, f, ensure_ascii=False, indent=2)
        print(f"💾 Данные записаны в habitgarden.json ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}).")
