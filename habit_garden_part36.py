# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: HabitGarden
def verify_integrity(db):
    errors = []
    for i, habit in enumerate(db.habits):
        if habit["status"] not in ("active", "completed", "paused"):
            errors.append(f"habit[{i}] invalid status: {habit['status']}")
        if habit.get("streak", 0) < 0:
            errors.append(f"habit[{i}] negative streak: {habit['streak']}")
        if habit.get("level", 0) < 0:
            errors.append(f"habit[{i}] negative level: {habit['level']}")
        if habit.get("created_at") > habit.get("updated_at", ""):
            errors.append(f"habit[{i}] timestamps inverted")
        if habit.get("notes") is not None and not isinstance(habit["notes"], str):
            errors.append(f"habit[{i}] notes not a string")

    if errors:
        print("Integrity check failed:")
        for e in errors:
            print(f"  - {e}")
        return False
    return True


def repair_simple_issues(db):
    repaired = 0
    for i, habit in enumerate(db.habits):
        if habit.get("status") not in ("active", "completed", "paused"):
            habit["status"] = "active"
            repaired += 1
        if habit.get("streak", 0) < 0:
            habit["streak"] = 0
            repaired += 1
        if habit.get("level", 0) < 0:
            habit["level"] = 0
            repaired += 1
        if habit.get("created_at", "") > habit.get("updated_at", ""):
            habit["updated_at"] = habit["created_at"]
            repaired += 1
        if habit.get("notes") is not None and not isinstance(habit["notes"], str):
            habit["notes"] = ""
            repaired += 1
    if repaired:
        print(f"Repaired {repaired} issues in habits.")
    return repaired
