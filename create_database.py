import sqlite3

class database:
	def __init__(self):
		pass
	def create_db(self):
		print("SQL Database creating...")
		self.conn = sqlite3.connect("Database.db")
		print("SQL Database Created Successfully!!")
		self.c = self.conn.cursor()
	def create_table(self):
		self.c.execute('''CREATE TABLE `1` (`Name`	REAL,`Email`	REAL,`Gender`	REAL,`Phone Number`	REAL)''')
		return self.c , self.conn
	
