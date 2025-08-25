# Basic To-Do List App using Python (Console-Based)

# We'll use a list to store all the tasks temporarily (not saved to file)
tasks = []

def show_options():
    print("\n----- What do you want to do? -----")
    print("1. Show all tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Exit")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks added yet.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("✅ Task added!")

def delete_task():
    show_tasks()
    try:
        choice = int(input("Enter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"❌ Removed: {removed}")
        else:
            print("⚠️ Invalid number!")
    except:
        print("⚠️ Please enter a valid number.")

# Main program loop
while True:
    show_options()
    user_input = input("Choose an option (1–4): ")

    if user_input == '1':
        show_tasks()
    elif user_input == '2':
        add_task()
    elif user_input == '3':
        delete_task()
    elif user_input == '4':
        print("Goodbye! 👋")
        break
    else:
        print("Invalid input! Try again.")
