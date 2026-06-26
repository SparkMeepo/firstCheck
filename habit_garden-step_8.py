# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: HabitGarden
import sys

def print_menu():
    print("\n=== HabitGarden Menu ===")
    print("1. Добавить привычку")
    print("2. Просмотреть прогресс")
    print("3. Удалить привычку")
    print("4. Выход")
    return input("Выберите действие (1-4): ")

def add_habit():
    name = input("Название привычки: ").strip()
    if not name: return False
    try:
        days = int(input("Количество дней подряд: "))
        notes = input("Заметка (опционально): ").strip() or ""
        print(f"Привычка '{name}' добавлена на {days} дней.")
        return True
    except ValueError:
        print("Ошибка: количество дней должно быть числом.")
        return False

def show_progress():
    habits = get_habits_from_file()  # Предполагается, что эта функция уже существует в проекте
    if not habits:
        print("Нет сохраненных привычек.")
        return
    for h in habits:
        print(f"Привычка: {h['name']}, Дней подряд: {h['streak']}, Заметка: {h.get('notes', '')}")

def delete_habit():
    name = input("Название привычки для удаления: ").strip()
    habits = get_habits_from_file()
    if not habits: return False
    for i, h in enumerate(habits):
        if h['name'] == name:
            del habits[i]
            save_habits_to_file(habits)  # Предполагается, что эта функция уже существует в проекте
            print(f"Привычка '{name}' удалена.")
            return True
    print("Привычка не найдена.")
    return False

def main():
    while True:
        choice = print_menu()
        if choice == "1": add_habit()
        elif choice == "2": show_progress()
        elif choice == "3": delete_habit()
        elif choice == "4": break
        else: print("Неверный выбор.")

if __name__ == "__main__":
    main()
