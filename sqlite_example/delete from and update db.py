import sqlite3

db = sqlite3.connect('employee.sqlite')
cursor = db.cursor()

import datetime
# today = datetime.datetime.now().today()


# DELETE:
# db.execute('DELETE FROM salary WHERE id = 1001')
# db.commit()

# UPDATE:
# db.execute('Update salary SET amount = 25000 WHERE id = 1002')
# db.commit()


# ****** SQL INJECTION concept: ********
# perform any code unintentionally. we should avoid this problem to happen.

# salary_id= input('enter id from salary table')
# cursor.executescript('Update salary SET amount ={} WHERE id = {}'.format(3000,salary_id))

# if we enter "1001;drop table salary" then we have INJECTION. and salary table will be deleted.

# 1- never use "executescript" to get the several query statements. instead we should use the "execute" frequently.
# 2- for parameter that get value from out of database with "input", never use ".format".
# ".format" is allowed for parameter that get value from (inside) database.



# **** replacement field: ****
# use replacement field("?" in sqlite, "%" in mysql, to get value from out of database with "input".

# cursor.execute('UPDATE salary SET amount =? WHERE id = ?',(6000,salary_id))
# db.commit()
# cursor.close()



# cursor.execute('INSERT INTO salary VALUES (1001,20000,2022-09-06)')
# cursor.execute('INSERT INTO salary VALUES (1003,50000,2022-09-06)')


# *** cursor: ***
# cursor is like a generator. so we can itterate through object assign with it.
salary_records = cursor.execute('SELECT * FROM salary')
print(salary_records)
for item in salary_records:
    print(item)
print('*******************')
for item in salary_records:
    print(item)
# LAST CODE PRINT NOTHING. because cursor is a generator. so when we call query with cursor, we can use it for once.
# for second use of query, we need to rerun the query.

# some method of db and cursor:

# fetchone: return a record where cursor is there.
print('*******')
salary_records = cursor.execute('SELECT * FROM salary')
print(cursor.fetchone()) #-------> line 1
print(cursor.fetchone()) #-------> line 2

# fetchall: return all records in format of list[].

# rowcount: return int that is  number of records in the database, changed due to query.
# if = -1 means that records are not changed due to query.

# lastrowid: return number of row of the last record in the database that changed due to query.


db.commit()
cursor.close()
db.close()





















