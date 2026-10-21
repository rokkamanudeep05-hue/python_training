
from tracker_manager import TaskManager

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

