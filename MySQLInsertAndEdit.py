from datetime import date
import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="bd")
cursor = db_connection.cursor()
sql = "INSERT INTO user (name, cpf) VALUES (%s, %s)"
values = ("Maria", "025.658.698-55")
cursor.execute(sql, values)
current_date = date.today()
formatted_date = current_date.strftime('%d/%m/%Y')

print(formatted_date)
print("\n")
print(cursor.rowcount, "record inserted.")
print("\n")

sql = ("SELECT id, name, cpf FROM user")
cursor.execute(sql)

for (id, name, cpf) in cursor:
  print(id, name, cpf)
print("\n")

sql = ("update user set name = 'Regina Phalanges' where cpf='025.658.698-55'")
cursor.execute(sql)

print(cursor.rowcount, "record updated.")
print("\n")

sql = ("SELECT id, name, cpf FROM user")
cursor.execute(sql)

for (id, name, cpf) in cursor:
  print(id, name, cpf)
  
cursor.close()
db_connection.commit()
db_connection.close()