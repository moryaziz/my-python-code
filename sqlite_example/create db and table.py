import sqlite3

db = sqlite3.connect('employee.sqlite')
cursor = db.cursor()
# its better to don't work with db, instead we are using the "cursor".

# create database with name of 'employee.sqlite'.

# CRUD process:

# create:

# create_query =  'CREATE TABLE IF NOT EXISTS people ('\
#                 'id INTEGER PRIMARY KEY, '\
#                 'name TEXT NOT NULL, '\
#                 'department TEXT DEFAULT UNKNOWN)'

# cursor.execute(create_query)

# create_query =  'CREATE TABLE IF NOT EXISTS salary ('\
#                 'id INTEGER, '\
#                 'amount INTEGER NOT NULL, '\
#                 'date TIMESTAMP)'

# cursor.execute(create_query)
# for perform and execute every query code: you must 'execute()' it.

# INSERT:

# cursor.execute('INSERT INTO people (id , name , department) VALUES(1001,"mehdi","IT")')
#
# db.commit()
# for make any change into database after execute the code, we must perform 'commit()'.

# INSERT:
# import datetime
# today = datetime.date.today()
# cursor.execute('INSERT INTO salary VALUES (1001,15000,"{}")'.format(today))
# cursor.execute('INSERT INTO salary VALUES (1002,20000,"{}")'.format(today))

# db.commit()












db.close()
# we must close database after out job.





















