import os
class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def add_task(self, task):
        """Add a task to the to-do list."""
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")
        self.save_tasks()

    def remove_task(self, task):
        """Remove a task from the to-do list."""
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed successfully!")
            self.save_tasks()
        else:
            print(f"Task '{task}' not found!")

    def view_tasks(self):
        """Display all tasks in the to-do list."""
        if not self.tasks:
            print("No tasks in your to-do list.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def save_tasks(self):
        """Save tasks to a file."""
        with open('todo_list.txt', 'w') as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def load_tasks(self):
        """Load tasks from a file."""
        if os.path.exists('todo_list.txt'):
            with open('todo_list.txt', 'r') as file:
                tasks = file.read().splitlines()
            return tasks
        return []

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")

def main():
    todo_list = TodoList()

    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            task = input("Enter the task to add: ").strip()
            if task:
                todo_list.add_task(task)
            else:
                print("Task cannot be empty!")

        elif choice == '2':
            task = input("Enter the task to remove: ").strip()
            todo_list.remove_task(task)

        elif choice == '3':
            todo_list.view_tasks()

        elif choice == '4':
            print("Exiting the to-do list application.")
            break

        else:
            print("Invalid choice! Please select a valid option.")

main()
