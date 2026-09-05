# === Stage 43: Добавь пагинацию длинных списков ===
# Project: HabitGarden
def paginate(items, page_size=10):
    pages = []
    for i in range(0, len(items), page_size):
        pages.append(items[i:i + page_size])
    return pages
