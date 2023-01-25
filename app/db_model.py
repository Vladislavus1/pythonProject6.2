import sqlite3

connection = sqlite3.connect("app.db")
print("DB success")

connection.execute("CREATE TABLE info_table (name TEXT, password TEXT)")
print("info_table success")

connection.close()