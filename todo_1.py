def printMenu():
    print('Todo List Menu:')
    print('1. View Tasks')
    print('2. Add a Task')
    print('3. Remove a Task')
    print('4. Exit')

def userChoice():
    while True:
        valid_choice = ('1','2','3','4')
        choice = input("Enter your choice: ")
        if choice not in valid_choice:
            print('Invalid choice!')
        else:
            break
    return choice
    
def taskView(tasks):
    if not tasks:
        print('No task in your queue..')
        return
    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')

def addTask(tasks):
    while True:
        task = input('Enter the task: ').strip('')
        if len(task) != 0:
            tasks.append(task)
            print("You added new task in your list.")
            break
        else:
            print('Invalid Task')
def removeTask(tasks):
    taskView(tasks)
    while True:
        try:
            task_number = int(input('Which task number you want to delete? '))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid task number.')



def main():
    tasks = []
    while True:
        printMenu()
        choice = userChoice()
        if choice == '1':
            taskView(tasks)
        elif choice == '2':
            addTask(tasks)
        elif choice == '3':
            removeTask(tasks)
        else:
            break

main()