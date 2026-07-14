# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: HabitGarden
def add_tag(habit, tag_name):
    if not habit.tags:
        habit.tags = []
    if tag_name not in habit.tags:
        habit.tags.append(tag_name)
        return True
    return False


def remove_tag(habit, tag_name):
    if tag_name in habit.tags:
        habit.tags.remove(tag_name)
        return True
    return False
