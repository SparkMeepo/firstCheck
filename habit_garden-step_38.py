# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: HabitGarden
import unittest
from datetime import datetime, timedelta

class HabitGardenEdgeCases(unittest.TestCase):
    def setUp(self):
        from HabitGarden import HabitGarden
        self.app = HabitGarden()

    def test_empty_habit_list(self):
        self.assertEqual(self.app.habits, [])

    def test_add_duplicate_habit(self):
        self.app.add_habit("Reading", "daily")
        self.app.add_habit("Reading", "daily")
        self.assertEqual(len(self.app.habits), 1)
        self.assertEqual(self.app.habits[0].name, "Reading")

    def test_add_habit_invalid_frequency(self):
        with self.assertRaises(ValueError):
            self.app.add_habit("Test", "invalid")

    def test_log_streak_invalid_date(self):
        habit = self.app.habits[0] if self.app.habits else self.app.add_habit("Test", "daily")
        with self.assertRaises(ValueError):
            habit.log_streak("not-a-date")

    def test_get_next_habit_no_habits(self):
        self.assertIsNone(self.app.get_next_habit())

    def test_get_next_habit_no_due(self):
        self.app.add_habit("Reading", "weekly")
        self.assertIsNone(self.app.get_next_habit())

    def test_get_next_habit_due_today(self):
        self.app.add_habit("Reading", "daily")
        self.assertEqual(self.app.get_next_habit().name, "Reading")

    def test_get_next_habit_due_later(self):
        self.app.add_habit("Reading", "weekly")
        self.assertIsNone(self.app.get_next_habit())

    def test_get_next_habit_multiple_due(self):
        self.app.add_habit("Reading", "daily")
        self.app.add_habit("Writing", "daily")
        self.assertEqual(self.app.get_next_habit().name, "Reading")

    def test_add_note_empty(self):
        self.assertIsNone(self.app.add_note("Test"))

    def test_add_note_with_content(self):
        note = self.app.add_note("Test note")
        self.assertEqual(note.content, "Test note")

    def test_mark_note_read(self):
        note = self.app.add_note("Test note")
        self.assertFalse(note.is_read)
        note.mark_read()
        self.assertTrue(note.is_read)

    def test_mark_note_read_twice(self):
        note = self.app.add_note("Test note")
        note.mark_read()
        note.mark_read()
        self.assertTrue(note.is_read)

    def test_get_read_notes(self):
        self.app.add_note("Read note")
        self.app.add_note("Unread note")
        self.app.habits[0].log_streak("2023-01-01")
        self.app.habits[0].log_streak("2023-01-02")
        self.app.habits[0].log_streak("2023-01-03")
        read_notes = self.app.get_read_notes()
        self.assertEqual(len(read_notes), 1)
        self.assertEqual(read_notes[0].content, "Read note")

    def test_get_unread_notes(self):
        self.app.add_note("Read note")
        self.app.add_note("Unread note")
        self.app.habits[0].log_streak("2023-01-01")
        self.app.habits[0].log_streak("2023-01-02")
        self.app.habits[0].log_streak("2023-01-03")
        unread_notes = self.app.get_unread_notes()
        self.assertEqual(len(unread_notes), 1)
        self.assertEqual(unread_notes[0].content, "Unread note")

    def test_add_reminder_empty(self):
        self.assertIsNone(self.app.add_reminder("Test reminder"))

    def test_add_reminder_with_content(self):
        reminder = self.app.add_reminder("Test reminder")
        self.assertEqual(reminder.content, "Test reminder")

    def test_mark_reminder_done(self):
        reminder = self.app.add_reminder("Test reminder")
        self.assertFalse(reminder.is_done)
        reminder.mark_done()
        self.assertTrue(reminder.is_done)

    def test_mark_reminder_done_twice(self):
        reminder = self.app.add_reminder("Test reminder")
        reminder.mark_done()
        reminder.mark_done()
        self.assertTrue(reminder.is_done)

    def test_get_done_reminders(self):
        self.app.add_reminder("Done reminder")
        self.app.add_reminder("Not done reminder")
        self.app.habits[0].log_streak("2023-01-01")
        self.app.habits[0].log_streak("2023-01-02")
        self.app.habits[0].log_streak("2023-01-03")
        done_reminders = self.app.get_done_reminders()
        self.assertEqual(len(done_reminders), 1)
        self.assertEqual(done_reminders[0].content, "Done reminder")

    def test_get_not_done_reminders(self):
        self.app.add_reminder("Done reminder")
        self.app.add_reminder("Not done reminder")
        self.app.habits[0].log_streak("2023-01-01")
        self.app.habits[0].log_streak("2023-01-02")
        self.app.habits[0].log_streak("2023-01-03")
        not_done_reminders = self.app.get_not_done_reminders()
        self.assertEqual(len(not_done_reminders), 1)
        self.assertEqual(not_done_reminders[0].content, "Not done reminder")
