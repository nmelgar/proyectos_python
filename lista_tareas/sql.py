import mysql.connector

# create db connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hola123-",
    database="todo_list"
)

# create cursor
mycursor = mydb.cursor()
