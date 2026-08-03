# === Stage 32: Добавь журнал действий пользователя ===
# Project: HabitGarden
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, user_name: str, action_type: str, details: dict) -> None:
        entry = {
            "timestamp": datetime.now().isoformat(),
            "user": user_name,
            "type": action_type,
            **details
        }
        self.entries.append(entry)

    def get_recent(self, count=5):
        return self.entries[-count:] if len(self.entries) >= count else list(self.entries)
