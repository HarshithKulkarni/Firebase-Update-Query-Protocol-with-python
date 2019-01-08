import sqlite3


print("SQL Database creating...")
conn = sqlite3.connect("Database.db")
print("SQL Database Created Successfully!!")
c = conn.cursor()
c.execute('''CREATE TABLE `1` (`Name`	REAL,`Email`	REAL,`Gender`	REAL,`Phone Number`	REAL)''')

"""c_file = open("c_file.txt","w")
c = str(c)
c_file.write(c)
c_file.close()

conn_file = open("conn_file.txt","w")
conn = str(conn)
conn_file.write(conn)
conn_file.close()"""
