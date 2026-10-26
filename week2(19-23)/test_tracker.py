
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

    # 15. Filter pending tasks
    def test_filter_pending_tasks(self) -> None:
        self.manager.add_task("Pending task")
        task = self.manager.add_task("Completed task")
        self.manager.complete_task(task["id"])

        result = self.manager.filter_tasks("pending")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Pending task")

    # 16. Filter completed tasks
    def test_filter_completed_tasks(self) -> None:
        task = self.manager.add_task("Completed task")
        self.manager.complete_task(task["id"])
        self.manager.add_task("Pending task")

        result = self.manager.filter_tasks("completed")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Completed task")

    # 17. Filter all tasks
    def test_filter_all_tasks(self) -> None:
        self.manager.add_task("Task one")
        self.manager.add_task("Task two")

        result = self.manager.filter_tasks("all")

        self.assertEqual(len(result), 2)

    # 18. Invalid filter status is rejected
    def test_invalid_filter_status_is_rejected(self) -> None:
        with pytest.raises(ValueError):
            self.manager.filter_tasks("invalid")

    # 19. Update a task title
    def test_update_task(self) -> None:
        task = self.manager.add_task("Old title")

        self.manager.update_task(task["id"], "New title")

        self.assertEqual(
            self.manager.find_task(task["id"])["title"],
            "New title",
        )

    # 20. Updated title is saved to JSON
    def test_update_task_persists(self) -> None:
        task = self.manager.add_task("Old title")

        self.manager.update_task(task["id"], "New title")

        reloaded = TaskManager(self.file_path)

        self.assertEqual(
            reloaded.find_task(task["id"])["title"],
            "New title",
        )

    # 21. Empty updated title is rejected
    def test_empty_updated_title_is_rejected(self) -> None:
        task = self.manager.add_task("Python")

        with pytest.raises(ValueError):
            self.manager.update_task(task["id"], "")

    # 22. Updating an unknown task ID is rejected
    def test_update_unknown_task_id_is_rejected(self) -> None:
        with pytest.raises(ValueError):
            self.manager.update_task(999, "New title")

    # 23. Listing tasks returns all tasks
    def test_list_tasks(self) -> None:
        self.manager.add_task("Task one")
        self.manager.add_task("Task two")

        result = self.manager.list_tasks()

        self.assertEqual(len(result), 2)

    # 24. Invalid task ID type is rejected
    def test_invalid_task_id_type_is_rejected(self) -> None:
        with pytest.raises(ValueError):
            self.manager.delete_task(1.5)  # type: ignore[arg-type]

    # 25. Invalid completed value in stored JSON is rejected
    def test_invalid_completed_value_is_rejected(self) -> None:
        invalid_tasks = [
            {"id": 1, "title": "Python", "completed": "yes"}
        ]

        self.file_path.write_text(
            json.dumps(invalid_tasks),
            encoding="utf-8",
        )

        with pytest.raises(ValueError):
            TaskManager(self.file_path)

    # 26. Invalid stored task ID is rejected
    def test_invalid_stored_task_id_is_rejected(self) -> None:
        invalid_tasks = [
            {"id": 0, "title": "Python", "completed": False}
        ]

        self.file_path.write_text(
            json.dumps(invalid_tasks),
            encoding="utf-8",
        )

        with pytest.raises(ValueError):
            TaskManager(self.file_path)

    # 27. Empty title in stored JSON is rejected
    def test_empty_stored_title_is_rejected(self) -> None:
        invalid_tasks = [
            {"id": 1, "title": "   ", "completed": False}
        ]

        self.file_path.write_text(
            json.dumps(invalid_tasks),
            encoding="utf-8",
        )

        with pytest.raises(ValueError):
            TaskManager(self.file_path)


if __name__ == "__main__":
    unittest.main()


