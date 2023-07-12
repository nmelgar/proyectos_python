from sql import *


def menu(menu_items):
    print("-----------------------")
    print("Choose an option")
    print("-----------------------\n")
    counter = 1
    for item in menu_items:
        print(f"{counter}. {item}")
        counter += 1


def add_task(user_input):
    sql = "INSERT INTO todo (task) VALUES (%s)"
    data_values = (f"{user_input}",)
    mycursor.execute(sql, data_values)
    mydb.commit()

    print("Task added successfully!")


def display_tasks():
    # check todo table is empty
    count = "SELECT COUNT(*) FROM todo"
    mycursor.execute(count)
    row = mycursor.fetchone()
    first_item = row[0]

    if first_item == 0:
        result = print("\nNo tasks for today\n")
        return result
    else:
        sql = "SELECT task FROM todo"
        mycursor.execute(sql)
        # obtener todos los registros de la tabla
        result = mycursor.fetchall()
        counter = 1
        print("\n")
        for item in result:
            # acceder al primer elemento de cada tupla, pero tupla solo tiene un elemento
            print(f"{counter}. {item[0]}")
            counter += 1


def update_task():
    user_input = input("Select a task number: ")
    try:
        user_input = int(user_input) - 1
        # get all the elements form the table
        sql_table = "SELECT * FROM todo"
        mycursor.execute(sql_table)
        myresult = mycursor.fetchall()

        # get element individually
        tuple_index = user_input
        tuple_task_value = 1
        tuple_value = myresult[tuple_index][tuple_task_value]

        # update task
        updated_task = input("Add new task: ")
        sql = "UPDATE todo SET task = %s WHERE task = %s"
        value = (updated_task, tuple_value)
        mycursor.execute(sql, value)
        mydb.commit()
        print("\nTask updated successfully!\n")

    except ValueError:
        print("Please enter a valid number.")
