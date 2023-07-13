from functions import *
from sql import *

menu_items = ["Add task", "Edit task", "Delete task", "Exit"]
print("\n|--------------|")
print("|--TO-DO LIST--|")
run = True

while run:
    display_tasks()
    menu(menu_items)
    user_choice = input("\nChoose an option: ")

    try:
        user_choice = int(user_choice)
        if user_choice == 1:
            user_input = input("\nAdd new task: ")
            add_task(user_input)
        elif user_choice == 2:
            update_task()
        elif user_choice == 3:
            delete_task()
        elif user_choice == 4:
            run = False
            print("\nPlease come back later :)!")
        else:
            print("\nPlease enter a valid number")

    except ValueError:
        print("\nPlease enter a valid number.")
