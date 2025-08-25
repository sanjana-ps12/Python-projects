tasks = []

# Add's the new tasks
def addTask():
    task = input("Enter a new Task: ")
    tasks.append(task)
    print(f"Task '{task}' added to your list.")

# Displays all the task that has been added to the list
def listTasks():
    if not tasks:
        print("No new Task yet!!")
    else:
        print("Your current tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task {index}. {task}")

# Delete's the selected tasks
def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Choose the task to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            deletedTask = tasks.pop(taskToDelete)
            print(f"Task '{deletedTask}' has been removed.")
        else:
            print(f"Task '{deletedTask}' was not found.")
    except:
        print("Invalid input")

# Marks the task has completed 
def doneTasks():
    listTasks()
    taskToDone = int(input("Choose the task to mark it as done: "))
    if taskToDone >= 0 and taskToDone < len(tasks):
        print(f"{tasks[taskToDone]} marked as done.")
        tasks[taskToDone] += "(done)"

# Displays the pending tasks that is not completed
def leftTasks():
    if not tasks:
        print("No pending tasks!!")
    else:
        print("Pending tasks:")
        for index, task in enumerate(tasks):
            if "(done)" not in task:
                print(f"Task {index}. {task}")

# Renames the task
def updateTasks():
    listTasks()
    taskToUpdate = int(input("Choose the task to update: "))
    if taskToUpdate >= 0 and taskToUpdate < len(tasks):
        updatedTask = input("rename the task: ")
        tasks[taskToUpdate] = updatedTask
        print(f"Task {taskToUpdate} has been updated.")
    else:
        print("Invalid task selection.")

# Main file
if __name__ == "__main__":
    print("~ ~ ~ WELCOME TO DO-TO LIST ~ ~ ~")
    while True:
        print("----------------------------------")
        print("Select an options")
        print("1. ADD TASK")
        print("2. DELETE TASK")
        print("3. LIST ALL TASK")
        print("4. MARK AS DONE")
        print("5. PENDING TASKS")
        print("6. RENAME TASK")
        print("7. QUIT")
        print("----------------------------------")
        choice = input("Enter your choice: ")
        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif(choice == "4"):
            doneTasks()
        elif(choice == "5"):
            leftTasks()
        elif(choice == "6"):
            updateTasks()  
        elif(choice == "7"):
            break
        else:
            print("Invalid input. Please enter again!")
    print("THANKS FOR USING TO-DO LIST. HAVE AN NICE DAY :)")
