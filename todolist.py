#ninth program made | partially myself and tutorial
tasks = []

def addTask():
    task = input("Please enter a task to complete: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to the list")

def listTasks():
    if not tasks:
        print("There are currently no tasks.")
    else:
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # of the task to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} was deleted.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input.")

if __name__ == "__main__":
    print("Welcome to my to-do list app!")
    while True:
        print("\n")
        print("Please select one of the following options.")
        print("-------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List current tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if(choice == "1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTasks()
        elif (choice == "4"):
           break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye!")
