
import json
import tempfile
import unittest
from pathlib import Path

from tracker import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temp_dir.name) / "tasks.json"
        self.manager = TaskManager(self.file_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_task(self):
        task = self.manager.add_task("Learn Python")

        self.assertEqual(task["title"], "Learn Python")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.tasks), 1)

    def test_empty_title_is_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_complete_task(self):
        task = self.manager.add_task("Practice loops")

        self.manager.complete_task(task["id"])

        self.assertTrue(self.manager.tasks[0]["completed"])

    def test_delete_task(self):
        task = self.manager.add_task("Practice functions")

        self.manager.delete_task(task["id"])

        self.assertEqual(self.manager.tasks, [])

    def test_unknown_task_id_is_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.complete_task(999)

    def test_tasks_are_saved_and_loaded(self):
        self.manager.add_task("Learn JSON")

        another_manager = TaskManager(self.file_path)

        self.assertEqual(
            another_manager.tasks[0]["title"],
            "Learn JSON"
        )

    def test_invalid_json_is_rejected(self):
        self.file_path.write_text("{invalid json", encoding="utf-8")

        with self.assertRaises(ValueError):
            TaskManager(self.file_path)


if __name__ == "__main__":
    unittest.main()
