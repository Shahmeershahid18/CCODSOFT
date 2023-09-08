import os

# Define a global variable to store the to-do list
to_do_list = []

# Function to add a task to the to-do list
def add_task(task):
    to_do_list.append(task)
    print("Task added:", task)

# Function to list all tasks in the to-do list
def list_tasks():
    if not to_do_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}. {task}")

# Function to mark a task as complete
def mark_task_complete(task_index):
    if 1 <= task_index <= len(to_do_list):
        print(f"Marking task '{to_do_list[task_index - 1]}' as complete.")
        to_do_list.pop(task_index - 1)
    else:
        print("Invalid task index. Please enter a valid task number.")

# Function to delete a task from the to-do list
def delete_task(task_index):
    if 1 <= task_index <= len(to_do_list):
        print(f"Deleting task '{to_do_list[task_index - 1]}'.")
        to_do_list.pop(task_index - 1)
    else:
        print("Invalid task index. Please enter a valid task number.")

# Function to save the to-do list to a file
def save_to_file(filename):
    with open(filename, "w") as file:
        for task in to_do_list:
            file.write(task + "\n")

# Function to load tasks from a file
def load_from_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = file.read().splitlines()
            to_do_list.extend(tasks)
    else:
        print("File not found. Creating a new to-do list.")

# Main program loop
def main():
    filename = "to_do_list.txt"
    load_from_file(filename)
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save and Quit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as complete: "))
            mark_task_complete(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task number to delete: "))
            delete_task(task_index)
        elif choice == "5":
            save_to_file(filename)
            print("To-Do List saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()