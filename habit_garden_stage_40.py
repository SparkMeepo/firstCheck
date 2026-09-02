# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: HabitGarden
import argparse, sys

def main():
    parser = argparse.ArgumentParser(description="HabitGarden CLI")
    parser.add_argument("action", choices=["add", "list", "stats"], help="действие")
    parser.add_argument("--habit", type=str, help="название привычки")
    parser.add_argument("--series", type=int, help="количество серий")
    parser.add_argument("--note", type=str, help="заметка")
    parser.add_argument("--reminder", type=str, help="напоминание")
    args = parser.parse_args()
    if args.action == "add" and not args.habit:
        parser.error("--habit обязателен для add")
    print(f"Команда: {args.action}, привычка: {args.habit or '—'}")

if __name__ == "__main__":
    main()
