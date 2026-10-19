
import json
from pathlib import Path


class TaskManager:
    def __init__(self, file_path=None):
        if file_path is None:
            file_path = Path(__file__).with_name("tasks.json")

        self.file_path = Path(file_path)
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                tasks = json.load(file)

            if not isinstance(tasks, list):
                raise ValueError("Tasks file must contain a list.")

            return tasks

        except json.JSONDecodeError as error:
            raise ValueError("The tasks.json file contains invalid JSON.") from error

    def save_tasks(self):
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty.")

        task = {
            "id": max((item["id"] for item in self.tasks), default=0) + 1,
            "title": title.strip(),
            "completed": False
        }

        self.tasks.append(task)
        self.save_tasks()
        return task

    def complete_task(self, task_id):
        task = self.find_task(task_id)
        task["completed"] = True
        self.save_tasks()

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        self.tasks.remove(task)
        self.save_tasks()

    def find_task(self, task_id):
        if not isinstance(task_id, int) or isinstance(task_id, bool):
            raise ValueError("Task ID must be a number.")

        for task in self.tasks:
            if task["id"] == task_id:
                return task

        raise ValueError("Task ID not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for task in self.tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f'{task["id"]}. {task["title"]} - {status}')


def main():
    manager = TaskManager()

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
