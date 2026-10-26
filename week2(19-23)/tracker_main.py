


from tracker import TaskManager


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


