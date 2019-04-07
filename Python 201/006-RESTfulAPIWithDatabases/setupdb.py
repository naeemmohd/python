# import sqlites3 module
import sqlite3

# creating a connection - will create a file dbProducts.db in current location
conn = sqlite3.connect("dbProducts.db")
# creating a cursor do work on the database
curs = conn.cursor()

# create required tables tblUsers and tblProducts
# Data type 'INTEGER'  is used for auto-incrementing columns only othrwise you can use normal 'int'
sqlTblUsers = "CREATE TABLE IF NOT EXISTS tblUsers(id INTEGER PRIMARY KEY, email TEXT, username TEXT, password TEXT)"
sqlTblProducts = "CREATE TABLE IF NOT EXISTS tblProducts(name TEXT PRIMARY KEY, desc TEXT, price REAL, qty REAL)"
# execute the query
curs.execute(sqlTblUsers)
curs.execute(sqlTblProducts)
# commit changes
conn.commit()

#close connection
conn.close()