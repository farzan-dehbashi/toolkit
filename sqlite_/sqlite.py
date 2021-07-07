import sqlite3
# in memory database that will be deleted right after end of the program
#connection = sqlite3.conect(':memory:')
# saved databas:
connection = sqlite3.connect('sample.db')
# create a cursor ( what tells database what we wanna do)
cursor = connection.cursor()
# create a table
cursor.execute(""""
CREATE TABLE customers (

)
"""")