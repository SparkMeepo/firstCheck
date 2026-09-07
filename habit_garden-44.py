# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: HabitGarden
def backup_data(file_path, backup_dir="./backups"):
    """Создает резервную копию файла данных с датой в имени."""
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"habitgarden_{timestamp}.json")
    shutil.copy2(file_path, backup_path)
    print(f"Backup saved: {backup_path}")
    return backup_path
