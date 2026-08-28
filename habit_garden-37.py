# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: HabitGarden
import unittest
from datetime import datetime

def test_habit_tracker():
    # Unit-тесты для HabitGarden без внешних зависимостей
    class TestHabitTracker(unittest.TestCase):
        def test_add_habit(self):
            tracker = HabitTracker()
            tracker.add_habit("Водить воду", "Ежедневно")
            self.assertEqual(tracker.habits, ["Водить воду"])

        def test_add_streak(self):
            tracker = HabitTracker()
            tracker.add_habit("Водить воду", "Ежедневно")
            tracker.add_streak("Водить воду", 3)
            self.assertEqual(tracker.streaks["Водить воду"], 3)

        def test_add_note(self):
            tracker = HabitTracker()
            tracker.add_note("Водить воду", "Пить утром после сна")
            self.assertIn("Пить утром после сна", tracker.notes["Водить воду"])

        def test_add_reminder(self):
            tracker = HabitTracker()
            tracker.add_reminder("Водить воду", "10:00")
            self.assertIn("10:00", tracker.reminders["Водить воду"])

        def test_get_progress(self):
            tracker = HabitTracker()
            tracker.add_habit("Водить воду", "Ежедневно")
            tracker.add_streak("Водить воду", 7)
            progress = tracker.get_progress()
            self.assertIn("Водить воду", progress)

    unittest.main()

if __name__ == "__main__":
    test_habit_tracker()
