task_list = []

def add_task(task_name=None, status="Incomplete"):
    if task_name is None:
        task_name = input("\nEnter the task you would like to add to your To-Do List: ")

    task_list.append({"title": task_name, "status": status})
    print(f"{task_name} has been added to the To-Do List.")

    while True:
        choice = input("\nWould you like to add another task? (yes/no): ").lower()
        if choice == 'yes':
            add_task()
            break
        elif choice == 'no':
            print("\nYou will be returned to the main menu.")
            break
        else:
            print("\nYou have not made a valid entry - you will be returned to the main menu.")
            break

def view_tasks():
    if task_list:
        print("\nTo-Do List:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index} - {task['title']} [{task['status']}]")
    else:
        print("\nThe To-Do List is Empty.")

def mark_task_complete():
    view_tasks()
    task_number = int(input("Enter the number of the task you would like to mark as complete: ")) - 1
    if 0 <= task_number < len(task_list):
        task_list[task_number]['status'] = "Complete"
        print(f"{task_list[task_number]['title']} has been marked as complete.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter the number of the task you would like to delete: ")) - 1
    if 0 <= task_number < len(task_list):
        removed_task = task_list.pop(task_number)
        print(f"{removed_task['title']} has been deleted from the To-Do List.")
    else:
        print("Invalid task number.")

def quit_application():
    print("You are exiting the To-Do List App.")
    exit()

while True:
    try:
        print("\nWelcome to the To-Do List App!")
        print("\nMenu:")
        print("1. Add a Task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")

        menu_choice = int(input("\nEnter a number from the menu: "))

        if menu_choice == 1:
            add_task()
        elif menu_choice == 2:
            view_tasks()
        elif menu_choice == 3:
            mark_task_complete()
        elif menu_choice == 4:
            delete_task()
        elif menu_choice == 5:
            quit_application()
        else:
            print("\nPlease make a valid menu choice, enter a number from 1 to 5.")

    except ValueError:
        print("\nPlease make a valid menu choice, enter a number from 1 to 5.")