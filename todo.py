# declare a dictionary
# print the menu
def printMenu():
    print("Todo List Menu:")
    print("1. View Task")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")


def getChoice():
    while True:
        valid_choices = ('1','2','3','4')
        userChoice = input("Enter your choice: ")
        if userChoice not in valid_choices:
            print("Invalid choices")
        else:
            break
    return userChoice
def display_tasks(tasks):
    if not tasks:
        print('No tasks in the list.')
        return
    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')
def add_task(tasks):
    while True:
        task = input('Enter a new task: ').strip()
        if len(task) != 0:
            tasks.append(task)
            break
        else:
            print("Invalid task!")

def remove_task(tasks):
    display_tasks(tasks)
    while True:
        try:
            task_number = int(input('Enter the task number: '))
            #if task_number >= 1 and task_number <= len(tasks)
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                break
            else:
                raise ValueError     
        except ValueError:
            print('Invalid task number ')

def main():
    tasks = []
    while True:
        printMenu()
        
        choice = getChoice()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        else:
            break

main()

