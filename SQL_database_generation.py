from iteration_count import iter_count
from create_database import database
from firebase import firebase
import sqlite3

class sql:
	def __init__(self):
		self.name = []
		self.email = []
		self.gender  = []
		self.phone = []
		
		iter_count_obj = iter_count()
		self.count,self.count_all = iter_count_obj.get_count()
		

		count_file = open("count.txt","r")
		self.Saved_Count = count_file.read()
		count_file.close()
		self.Saved_Count = int(self.Saved_Count)
	

	def check_database_for_zero_entries(self):
		if(self.Saved_Count==0):
			self.database_obj = database()
			self.database_obj.create_db()
			self.c,self.conn = self.database_obj.create_table()
		else:
			self.conn = sqlite3.connect("Database.db")
			self.c = self.conn.cursor()
	

	def check_for_database_update(self):
		self.check_for_database_update()
		if(self.Saved_Count == (self.count)):
			
			print("The Database is not updated!!")
		
		else:
			
			print("The Database has been updated!!!")
			print("New Data has started to Update to SQL!!")
			print("Importing Data From Firebase...")
			fb = firebase.FirebaseApplication('https://image-db-d8b91.firebaseio.com/')
			print("Uploading Data To SQL...")
			for i in range(self.Saved_Count+1,self.count_all):
				self.name = fb.get('/Tech-Tailor/{}'.format(i),'Name')
				self.email  = fb.get('/Tech-Tailor/{}'.format(i),'Email')
				self.gender = fb.get('/Tech-Tailor/{}'.format(i),'Gender')
				self.phone = fb.get('/Tech-Tailor/{}'.format(i),'Phone Number')
				self.c.execute('''INSERT INTO `1` VALUES(?,?,?,?)''',(self.name,self.email,self.gender,self.phone))
				self.conn.commit()
		file = open("count.txt","w")
		file.write(str(self.Saved_Count))
		file.close()



if(__name__ == "__main__"):

	sql_obj = sql()

	sql_obj.check_for_database_update()
