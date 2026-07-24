# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: HabitGarden
def parse_date(date_str):
    """Parse date string into a datetime.date object, with clear error messages."""
    if not isinstance(date_str, str) or not date_str.strip():
        return None
    
    valid_formats = [
        "%Y-%m-%d",      # 2024-01-15
        "%d.%m.%Y",      # 15.01.2024
        "%d/%m/%Y",      # 15/01/2024
        "%Y/%m/%d",      # 2024/01/15
        "%d-%m-%Y",      # 15-01-2024
    ]
    
    date_str = date_str.strip()
    
    for fmt in valid_formats:
        try:
            return datetime.date.fromisoformat(date_str) if fmt == "%Y-%m-%d" else datetime.datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    
    raise ValueError(f"Не удалось распарсить дату '{date_str}'. Поддерживаемые форматы: YYYY-MM-DD, DD.MM.YYYY, DD/MM/YYYY")

# Пример использования:
try:
    current_date = parse_date("2024-12-31")
    print(f"Текущая дата: {current_date}")
except ValueError as e:
    print(f"Ошибка: {e}")
