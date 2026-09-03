# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: HabitGarden
def dry_run(operation, data, description=""):
    if not hasattr(data, "dry_run_mode"):
        data.dry_run_mode = False
    if data.dry_run_mode:
        print(f"[DRY-RUN] {description}: {operation} -> {data}")
        return operation
    return operation
