# === Stage 17: Добавь группировку записей по категориям ===
# Project: HabitGarden
CATEGORIES = ["Здоровье", "Развитие", "Креативность", "Социальные"]


def group_entries_by_category(entries):
    grouped = {cat: [] for cat in CATEGORIES}
    for entry in entries:
        if not entry.get("category"):
            entry["category"] = "Развитие"
        grouped[entry["category"]].append(entry)
    return grouped


def render_grouped_table(grouped):
    lines = ["Категория\tПодписчиков", "------------------\t--------"]
    for cat, subs in grouped.items():
        if subs:
            lines.append(f"{cat}\t{len(subs)}")
    return "\n".join(lines)
