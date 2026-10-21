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

    def get_tasks(self) -> list[dict]:
        return self.tasks.copy()    