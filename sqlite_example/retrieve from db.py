import sqlite3

db = sqlite3.connect('employee.sqlite')
cursor = db.cursor()

# connect to database

people_query = cursor.execute('SELECT * FROM people')
for item in people_query:
    print (item)

# we have to assign execute(SELECT) to a parameter in order to loop into it.

id_name_query = cursor.execute('SELECT id,name FROM people')
for item in id_name_query:
    print (item)














