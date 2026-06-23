# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: HabitGarden
class HabitFilter:
    def __init__(self, records):
        self.records = records

    def filter_by_status(self, status=None):
        if not status:
            return list(self.records)
        return [r for r in self.records if r.get('status') == status]

    def filter_by_category(self, category=None):
        if not category:
            return list(self.records)
        return [r for r in self.records if r.get('category') == category]

    def filter_by_tags(self, tags=None):
        if not tags or not isinstance(tags, list):
            return list(self.records)
        filtered = []
        for record in self.records:
            record_tags = record.get('tags', [])
            if any(tag in record_tags for tag in tags):
                filtered.append(record)
        return filtered

    def apply_filters(self, status=None, category=None, tags=None):
        records = list(self.records)
        if status:
            records = self.filter_by_status(status)
        if category:
            records = self.filter_by_category(category)
        if tags:
            records = self.filter_by_tags(tags)
        return records
