# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: HabitGarden
class HabitSearch:
    def __init__(self, habits):
        self._habits = list(habits)
    
    def search(self, query=None, habit_type=None, category=None, tags=None):
        if not any([query, habit_type, category, tags]):
            return [h for h in self._habits]
        
        results = []
        query_lower = query.lower() if query else ""
        
        def matches(habit):
            q_match = (not query) or (query_lower in habit['name'].lower())
            t_match = (not habit_type) or (habit.get('type') == habit_type)
            c_match = (not category) or (habit.get('category') == category)
            
            if tags:
                tag_set = set(t.lower() for t in tags.split(','))
                h_tags = {t.strip().lower(): 0 for t in tag_set}
                habit_tags = [tag['name'].lower() for tag in habit.get('tags', [])]
                
                for ht in habit_tags:
                    if ht in h_tags:
                        h_tags[ht] += 1
                
                match_count = sum(h_tags.values())
                t_match = (not tags) or (match_count > 0)
            
            return q_match and t_match and c_match
        
        for habit in self._habits:
            if matches(habit):
                results.append(habit)
        
        return results
