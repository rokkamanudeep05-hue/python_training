
import json
from pathlib import Path
from typing import Any


class TaskManager:
    def __init__(self, file_path: str | Path | None = None) -> None:
        if file_path is None:
            file_path = Path(__file__).with_name("tasks.json")

        self.file_path = Path(file_path)
        self.tasks: list[dict[str, Any]] = self.load_tasks()

    def load_tasks(self) -> list[dict[str, Any]]:
        """Load tasks and validate the JSON data."""
        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                tasks = json.load(file)
        except json.JSONDecodeError as error:
            raise ValueError(
                "The tasks file contains invalid JSON."
            ) from error

        if not isinstance(tasks, list):
            raise ValueError("The tasks file must contain a list.")

        seen_ids: set[int] = set()

        for task in tasks:
            if not isinstance(task, dict):
                raise ValueError("Each task must be a dictionary.")

            task_id = task.get("id")
            title = task.get("title")
            completed = task.get("completed")

            if type(task_id) is not int or task_id <= 0:
                raise ValueError(
                    "Each task must have a positive integer ID."
                )

            if task_id in seen_ids:
                raise ValueError(f"Duplicate task ID: {task_id}.")

            if not isinstance(title, str) or not title.strip():
                raise ValueError(
                    "Each task must have a non-empty title."
                )

            if not isinstance(completed, bool):
                raise ValueError(
                    "The completed field must be True or False."
                )

            seen_ids.add(task_id)

        return tasks

    def save_tasks(
        self, tasks: list[dict[str, Any]] | None = None
    ) -> None:
        """Save tasks through a temporary file."""
        tasks_to_save = self.tasks if tasks is None else tasks
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        temp_path = self.file_path.with_suffix(
            self.file_path.suffix + ".tmp"
        )

        try:
            with temp_path.open("w", encoding="utf-8") as file:
                json.dump(tasks_to_save, file, indent=4)
                file.write("\n")

            temp_path.replace(self.file_path)

        except (OSError, TypeError, ValueError):
            try:
                temp_path.unlink(missing_ok=True)
            except OSError:
                pass
            raise

    @staticmethod
    def validate_task_id(task_id: int) -> None:
        """Validate a task ID."""
        if type(task_id) is not int or task_id <= 0:
            raise ValueError(
                "Task ID must be a positive integer."
            )

    def add_task(self, title: str) -> dict[str, Any]:
        """Create a new task."""
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty.")

        new_task = {
            "id": max(
                (task["id"] for task in self.tasks),
                default=0,
            ) + 1,
            "title": title.strip(),
            "completed": False,
        }

        updated_tasks = self.tasks + [new_task]
        self.save_tasks(updated_tasks)
        self.tasks = updated_tasks

        return new_task.copy()

    def find_task(self, task_id: int) -> dict[str, Any]:
        """Find a task by ID."""
        self.validate_task_id(task_id)

        for task in self.tasks:
            if task["id"] == task_id:
                return task

        raise ValueError(f"Task ID {task_id} was not found.")

    def list_tasks(self) -> list[dict[str, Any]]:
        """Return all tasks."""
        return [task.copy() for task in self.tasks]

    def filter_tasks(
        self, status: str
    ) -> list[dict[str, Any]]:
        """Filter tasks by all, pending, or completed status."""
        if status not in ("all", "pending", "completed"):
            raise ValueError(
                "Status must be 'all', 'pending', or 'completed'."
            )

        if status == "all":
            return self.list_tasks()

        is_completed = status == "completed"

        return [
            task.copy()
            for task in self.tasks
            if task["completed"] is is_completed
        ]

    def update_task(
        self, task_id: int, new_title: str
    ) -> None:
        """Update the title of an existing task."""
        if not isinstance(new_title, str) or not new_title.strip():
            raise ValueError("Task title cannot be empty.")

        self.find_task(task_id)

        updated_tasks = [
            {**task, "title": new_title.strip()}
            if task["id"] == task_id
            else task.copy()
            for task in self.tasks
        ]

        self.save_tasks(updated_tasks)
        self.tasks = updated_tasks

    def complete_task(self, task_id: int) -> None:
        """Mark a task as completed."""
        self.find_task(task_id)

        updated_tasks = [
            {**task, "completed": True}
            if task["id"] == task_id
            else task.copy()
            for task in self.tasks
        ]

        self.save_tasks(updated_tasks)
        self.tasks = updated_tasks

    def delete_task(self, task_id: int) -> None:
        """Delete a task."""
        self.find_task(task_id)

        updated_tasks = [
            task.copy()
            for task in self.tasks
            if task["id"] != task_id
        ]

        self.save_tasks(updated_tasks)
        self.tasks = updated_tasks

    def view_tasks(self) -> None:
        """Print all tasks."""
        if not self.tasks:
            print("No tasks found.")
            return

        for task in self.tasks:
            status = (
                "Completed" if task["completed"] else "Pending"
            )
            print(
                f'{task["id"]}. {task["title"]} - {status}'
            )




def main() -> None:
    manager = TaskManager()

    while True:
        print("\n===== TASK TRACKER =====")
        print("1. Add task")
        print("2. List all tasks")
        print("3. Filter tasks")
        print("4. Update task")
        print("5. Complete task")
        print("6. Delete task")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                title = input("Enter task title: ")
                task = manager.add_task(title)
                print(f"Task added with ID {task['id']}.")

            elif choice == "2":
                tasks = manager.list_tasks()
                if not tasks:
                    print("No tasks found.")
                for task in tasks:
                    status = "Completed" if task["completed"] else "Pending"
                    print(f"{task['id']}. {task['title']} - {status}")

            elif choice == "3":
                status = input(
                    "Enter status (all/pending/completed): "
                ).strip().lower()
                tasks = manager.filter_tasks(status)
                for task in tasks:
                    print(f"{task['id']}. {task['title']}")

                if not tasks:
                    print("No matching tasks found.")

            elif choice == "4":
                task_id = int(input("Enter task ID: "))
                title = input("Enter new title: ")
                manager.update_task(task_id, title)
                print("Task updated successfully.")

            elif choice == "5":
                task_id = int(input("Enter task ID: "))
                manager.complete_task(task_id)
                print("Task completed successfully.")

            elif choice == "6":
                task_id = int(input("Enter task ID: "))
                manager.delete_task(task_id)
                print("Task deleted successfully.")

            elif choice == "7":
                print("Exiting Task Tracker.")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 7.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()


