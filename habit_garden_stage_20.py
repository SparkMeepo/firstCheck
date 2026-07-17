# === Stage 20: Добавь восстановление записей из архива ===
# Project: HabitGarden
import json, os

ARCHIVE_FILE = "habits_archive.json"

def load_from_archive(archive_path):
    if not os.path.exists(archive_path):
        return []
    with open(archive_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "entries" in data:
        return data["entries"]
    return []

def restore_records(archive_path, target_file, max_restore=10):
    archive_entries = load_from_archive(archive_path)
    existing = set()
    try:
        with open(target_file, "r", encoding="utf-8") as f:
            current = json.load(f)
            if isinstance(current, list):
                existing = {json.dumps(h.get("id"), ensure_ascii=False) for h in current}
            elif isinstance(current, dict):
                entries = current.get("entries", [])
                existing = {json.dumps(h.get("id"), ensure_ascii=False) for h in entries}
    except Exception:
        pass

    restored = []
    for entry in archive_entries[:max_restore]:
        key = json.dumps(entry.get("id"), ensure_ascii=False)
        if key not in existing and "restored" not in entry:
            entry["restored"] = True
            restored.append(entry)

    if restored:
        with open(target_file, "a", encoding="utf-8") as f:
            json.dump(restored, f, ensure_ascii=False, indent=2)

    return restored
