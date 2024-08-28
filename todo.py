import os
tasks = []
def display_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added successfully.")

def update_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter the task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_no - 1] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter the task number to delete: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
      while True:
        display_menu()
        choice = input("\nEnter your choice (1/2/3/4/5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exited.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
