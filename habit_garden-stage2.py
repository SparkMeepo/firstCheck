# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: HabitGarden
class Habit:
    def __init__(self, name: str, streak=0):
        self.name = name.strip()
        if not self.name or len(self.name) > 50: raise ValueError("Имя привычки должно быть от 1 до 50 символов")
        self.streak = max(0, int(streak))

    def log_completion(self):
        self.streak += 1
        return self.streak

class Note:
    def __init__(self, content: str):
        self.content = content.strip() if content else ""
        if len(self.content) > 500: raise ValueError("Заметка не может превышать 500 символов")

def validate_input(data: dict) -> tuple[bool, list[str]]:
    errors = []
    if 'habit' in data and isinstance(data['habit'], str):
        try: Habit(name=data['habit'])
        except ValueError as e: errors.append(str(e))
    if 'note' in data and isinstance(data['note'], str):
        try: Note(content=data['note'])
        except ValueError as e: errors.append(str(e))
    return len(errors) == 0, errors

if __name__ == "__main__":
    test_data = {"habit": "Чтение", "note": "Короткая заметка"}
    is_valid, errs = validate_input(test_data)
    print(f"Валидация: {is_valid}, Ошибки: {errs}")
