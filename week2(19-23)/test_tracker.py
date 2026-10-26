

import json
import tempfile
import unittest
from pathlib import Path

import pytest
from tracker import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temp_dir.name) / "tasks.json"
        self.manager = TaskManager(self.file_path)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    # 1. Missing file starts with an empty task list
    def test_missing_file_starts_empty(self) -> None:
        self.assertEqual(self.manager.tasks, [])

    # 2. Adding a task saves it correctly
    def test_add_task(self) -> None:
        task = self.manager.add_task("Learn Python")

        self.assertEqual(task["id"], 1)
        self.assertEqual(task["title"], "Learn Python")
        self.assertFalse(task["completed"])

        saved = json.loads(
            self.file_path.read_text(encoding="utf-8")
        )
        self.assertEqual(saved, [task])

    # 3. Empty title is rejected
    def test_empty_title_is_rejected(self) -> None:
        with pytest.raises(ValueError):
            self.manager.add_task("")

        self.assertEqual(self.manager.tasks, [])

    # 4. Whitespace-only title is rejected
    def test_whitespace_title_is_rejected(self) -> None:
        with pytest.raises(ValueError):
            self.manager.add_task("   ")

        self.assertEqual(self.manager.tasks, [])

    # 5. Non-string title is rejected
    def test_non_string_title_is_rejected(self) -> None:
        with pytest.raises(ValueError):
            self.manager.add_task(None)  # type: ignore[arg-type]

        self.assertEqual(self.manager.tasks, [])

    # 6. Leading and trailing spaces are removed
    def test_title_is_stripped(self) -> None:
        task = self.manager.add_task("  Learn Python  ")

        self.assertEqual(task["title"], "Learn Python")

    # 7. Completing a task persists its status
    def test_complete_task(self) -> None:
        task = self.manager.add_task("Practice tests")
        self.manager.complete_task(task["id"])

        reloaded = TaskManager(self.file_path)
        self.assertTrue(reloaded.tasks[0]["completed"])

    # 8. Deleting a task removes it
    def test_delete_task(self) -> None:
        task = self.manager.add_task("Temporary task")
        self.manager.delete_task(task["id"])

        self.assertEqual(self.manager.tasks, [])
        self.assertEqual(TaskManager(self.file_path).tasks, [])

    # 9. Unknown task ID is rejected
    def test_unknown_task_id_is_rejected(self) -> None:
        with pytest.raises(ValueError):
            self.manager.complete_task(999)

    # 10. Invalid task ID is rejected
    def test_invalid_task_id_is_rejected(self) -> None:
        with pytest.raises(ValueError):
            self.manager.delete_task(0)

    # 11. Corrupt JSON is rejected without overwriting the file
    def test_corrupt_json_is_not_overwritten(self) -> None:
        original_content = '{"id": '
        self.file_path.write_text(
            original_content, encoding="utf-8"
        )

        with pytest.raises(ValueError):
            TaskManager(self.file_path)

        self.assertEqual(
            self.file_path.read_text(encoding="utf-8"),
            original_content,
        )

    # 12. Incorrect JSON structure is rejected
    def test_wrong_json_structure_is_rejected(self) -> None:
        self.file_path.write_text(
            '{"task": "Python"}', encoding="utf-8"
        )

        with pytest.raises(ValueError):
            TaskManager(self.file_path)

    # 13. Duplicate task IDs are rejected
    def test_duplicate_task_ids_are_rejected(self) -> None:
        duplicate_tasks = [
            {"id": 1, "title": "First", "completed": False},
            {"id": 1, "title": "Second", "completed": False},
        ]

        self.file_path.write_text(
            json.dumps(duplicate_tasks),
            encoding="utf-8",
        )

        with pytest.raises(ValueError):
            TaskManager(self.file_path)

    # 14. Invalid task record is rejected
    def test_invalid_task_record_is_rejected(self) -> None:
        invalid_tasks = [
            {"id": 1, "title": "Python"}
        ]

        self.file_path.write_text(
            json.dumps(invalid_tasks),
            encoding="utf-8",
        )

        with pytest.raises(ValueError):
            TaskManager(self.file_path)


if __name__ == "__main__":
    unittest.main()


