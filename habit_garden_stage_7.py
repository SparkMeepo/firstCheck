# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: HabitGarden
class HabitGarden:
    def __init__(self):
        self.records = []

    def add_record(self, title, priority=1, date=None, note=""):
        record = {
            "title": title,
            "priority": int(priority),
            "date": date or datetime.now(),
            "note": note
        }
        self.records.append(record)

    def get_sorted_records(self, sort_by="date", reverse=False):
        if sort_by == "priority":
            return sorted(self.records, key=lambda x: (x["priority"], x["title"]), reverse=reverse)
        elif sort_by == "name":
            return sorted(self.records, key=lambda x: x["title"].lower(), reverse=reverse)
        else:  # default to date
            return sorted(self.records, key=lambda x: x["date"], reverse=reverse)

    def get_records_for_date_range(self, start_date, end_date):
        filtered = [r for r in self.records if start_date <= r["date"] <= end_date]
        return self.get_sorted_records("date", reverse=True)
