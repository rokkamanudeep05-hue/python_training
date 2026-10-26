
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
            raise ValueError("The tasks file contains invalid JSON.") from error

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
                raise ValueError("Each task must have a positive integer ID.")

            if task_id in seen_ids:
                raise ValueError(f"Duplicate task ID: {task_id}.")

            if not isinstance(title, str) or not title.strip():
                raise ValueError("Each task must have a non-empty title.")

            if not isinstance(completed, bool):
                raise ValueError("The completed field must be True or False.")

            seen_ids.add(task_id)

        return tasks

    def save_tasks(
        self, tasks: list[dict[str, Any]] | None = None
    ) -> None:
        """Write tasks safely using a temporary file."""
        tasks_to_save = self.tasks if tasks is None else tasks
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
        if type(task_id) is not int or task_id <= 0:
            raise ValueError("Task ID must be a positive integer.")

    def add_task(self, title: str) -> dict[str, Any]:
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty.")

        new_task = {
            "id": max((task["id"] for task in self.tasks), default=0) + 1,
            "title": title.strip(),
            "completed": False,
        }

        updated_tasks = self.tasks + [new_task]
        self.save_tasks(updated_tasks)
        self.tasks = updated_tasks
        return new_task

    def find_task(self, task_id: int) -> dict[str, Any]:
        self.validate_task_id(task_id)

        for task in self.tasks:
            if task["id"] == task_id:
                return task

        raise ValueError(f"Task ID {task_id} was not found.")

    def complete_task(self, task_id: int) -> None:
        task = self.find_task(task_id)
        updated_tasks = [
            {**item, "completed": True}
            if item["id"] == task_id else item.copy()
            for item in self.tasks
        ]

        self.save_tasks(updated_tasks)
        self.tasks = updated_tasks

    def delete_task(self, task_id: int) -> None:
        self.find_task(task_id)
        updated_tasks = [
            item.copy() for item in self.tasks
            if item["id"] != task_id
        ]

        self.save_tasks(updated_tasks)
        self.tasks = updated_tasks

    def view_tasks(self) -> None:
        if not self.tasks:
            print("No tasks found.")
            return

        for task in self.tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f'{task["id"]}. {task["title"]} - {status}')



def main() -> None:
    try:
        manager = TaskManager()
    except (ValueError, OSError) as error:
        print(f"Unable to load tasks: {error}")
        return

    while True:
        print("\n--- Python Task Tracker ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                title = input("Enter task title: ")
                task = manager.add_task(title)
                print(f'Task added: {task["title"]}')

            elif choice == "2":
                manager.view_tasks()

            elif choice == "3":
                task_id = int(input("Enter task ID: "))
                manager.complete_task(task_id)
                print("Task completed successfully.")

            elif choice == "4":
                task_id = int(input("Enter task ID: "))
                manager.delete_task(task_id)
                print("Task deleted successfully.")

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 5.")

        except ValueError as error:
            print(f"Error: {error}")
        except OSError as error:
            print(f"File error: {error}")


if __name__ == "__main__":
    main()

