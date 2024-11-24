def printMenu():
    print("Todo List Menu")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")

def userChoice():
    while True: 
        choices = ("1","2","3","4")
        choice = input("Enter your choice: ")
        if choice not in choices:
            print("Invalid Choice")
        else:
            break
    return choice

def viewTask(tasks):
    if not tasks:
        print("No Tasks in the list.")
        return
    for index, item in enumerate(tasks, start=1):
        print(f"{index} . {item}")

def addTask(tasks):
    adding_task = input("Enter your task: ")
    tasks.append(adding_task)

def removingTask(tasks):
    while True:
        try:
            task = int(input("Which task you want to remove: "))
            if 1 <= task <= len(tasks):
                tasks.pop(task - 1)
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid Task number')

def main():
    tasks = []
    while True:
        printMenu()
        choice = userChoice()
        if choice == '1':
            viewTask(tasks)
        elif choice == '2':
            addTask(tasks)
        elif choice == '3':
            removingTask(tasks)
        else:
            break
main()

