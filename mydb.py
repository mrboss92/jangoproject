#installed connector

import mysql.connector

dataBase = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password ='mukesh99'
)

#prepare a cursor
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE prodb")
print("all done!!")