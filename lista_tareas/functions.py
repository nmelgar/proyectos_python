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
