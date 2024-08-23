import sys
from task_manager import TaskManager
from utils import Utils

FILE_PATH = 'tasks.json'


class TaskManagerCLI:
    def __init__(self) -> None:
        self.manager = TaskManager()
        self.load_tasks()
    
    def load_tasks(self) -> None:
        task_data = Utils.load_tasks_from_file(FILE_PATH)
        self.manager.load_from_dict_list(task_data)
    
    def save_tasks(self) -> None:
        Utils.save_tasks_to_file(FILE_PATH, self.manager.to_dict_list())
    
    @staticmethod
    def display_menu() -> None:
        print("""
Task Manager
1. Add Task
2. Delete Task
3. Mark Task as Completed
4. List Tasks
5. Exit
        """)
    
    def handle_choice(self) -> None:
        while True:
            self.display_menu()
            choice = input("Choose an option: ").strip()
            
            if choice == "1":
                description = input("Enter task description: ").strip()
                task = self.manager.add_task(description)
                print(f"Task '{task.description}' added successfully!")
            elif choice == "2":
                try:
                    task_id = int(input("Enter task ID to delete: ").strip())
                    if self.manager.delete_task(task_id):
                        print(f"Task {task_id} deleted successfully!")
                    else:
                        print(f"Task {task_id} not found.")
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            elif choice == "3":
                try:
                    task_id = int(input("Enter task ID to mark as completed: ").strip())
                    if self.manager.mark_task_as_completed(task_id):
                        print(f"Task {task_id} marked as completed!")
                    else:
                        print(f"Task {task_id} not found.")
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            elif choice == "4":
                tasks = self.manager.list_tasks()
                if not tasks:
                    print("No tasks found.")
                else:
                    for task in tasks:
                        print(task)
            elif choice == "5":
                self.save_tasks()
                print("Tasks saved. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    cli = TaskManagerCLI()
    cli.handle_choice()
