import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hola123-",
    database="todo_list"
)

# create cursor
mycursor = mydb.cursor()
# sql = "SELECT task FROM todo"
# mycursor.execute(sql)
# result = mycursor.fetchall()
# for x in result:
#     print(x)
# create db
# sql = "CREATE DATABASE todo_list"

# create table
# sql = "CREATE TABLE todo (id INT AUTO_INCREMENT PRIMARY KEY, task VARCHAR(255), created_at DATETIME DEFAULT CURRENT_TIMESTAMP)"
# mycursor.execute(sql)