import os
import json

FILENAME = "todo_list.json"
tasks = []

# Load tasks from file if exists
def load_tasks():
    global tasks
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            tasks = json.load(file)
        print("Tasks loaded successfully.")
    else:
        print("No existing task file found. Starting fresh.")

# Save tasks to file
def save_tasks():
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file)
    print("Tasks saved successfully.")

# Menu display
def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Exit")

# View current tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Add a new task
def add_task():
    task = input("Enter the new task: ")
    tasks.append(task)
    print("Task added!")

# Update an existing task
def update_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter updated task: ")
            tasks[task_num] = new_task
            print("Task updated!")
        except (IndexError, ValueError):
            print("Invalid task number.")

# Delete a task
def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: ")) - 1
            removed = tasks.pop(task_num)
            print(f"Task '{removed}' deleted.")
        except (IndexError, ValueError):
            print("Invalid task number.")

# Main program
def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose between 1 to 6.")

if __name__ == "__main__":
    main()
