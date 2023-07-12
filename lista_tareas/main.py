# 1 create database connection (completed)
# 2 display menu (completed)
#   display tasks before menu (completed)
# 3 add task to db (completed)
# 4 modify task ()
# 5 delete task
# 6 stop program

from functions import *
from sql import *

menu_items = ["Add task", "Edit task", "Delete task", "Exit"]

print("|--TO-DO LIST--|")
display_tasks()
menu(menu_items)

# user_input = input("Add your task: ")
# add_task(user_input)

# update_task()

# for x in myresult:
# print(myresult[1][1])

# def main():
#     print("Hello World")

# if __name__ == "__main__":
#     main()
