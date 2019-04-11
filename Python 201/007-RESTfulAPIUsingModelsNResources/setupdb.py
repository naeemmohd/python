# setupdb.py - code for setting up the database and the tables 
# execute this script as - ***python setupdb.py***
# import sqlites3 module
import sqlite3

# creating a connection - will create a file dbProducts.db in current location
dbConnection = sqlite3.connect("dbProducts.db")
# creating a cursor do work on the database
dbCursor = dbConnection.cursor()

# create required tables tblUsers and tblProducts
# Data type 'INTEGER'  is used for auto-incrementing columns only othrwise you can use normal 'int'
sqlTblUsers = "CREATE TABLE IF NOT EXISTS tblUsers(id INTEGER PRIMARY KEY, email TEXT, username TEXT, password TEXT)"
sqlTblProducts = "CREATE TABLE IF NOT EXISTS tblProducts(name TEXT PRIMARY KEY, desc TEXT, price REAL, qty REAL)"

# execute the query
dbCursor.execute(sqlTblUsers)
dbCursor.execute(sqlTblProducts)

# commit changes
dbConnection.commit()

#close dbConnection
dbConnection.close()