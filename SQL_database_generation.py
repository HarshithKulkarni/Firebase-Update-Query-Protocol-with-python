from iter_count import count
from firebase import firebase
import sqlite3



name = []
email = []
gender  = []
phone = []



def create_sql():
	print("SQL Database creating...")
	conn = sqlite3.connect("Database.db")
	print("SQL Database Created Successfully!!")
	c = conn.cursor()
	c.execute('''CREATE TABLE `1` (`Name`	REAL,`Email`	REAL,`Gender`	REAL,`Phone Number`	REAL)''')
	return (conn,c)


def import_and_write(conn,c):

	print("Importing Data From Firebase...")
	fb = firebase.FirebaseApplication('https://image-db-d8b91.firebaseio.com/')
	print("Uploading Data To SQL...")
	for i in range(1,(count)):
		name = fb.get('/Tech-Tailor/{}'.format(i),'Name')
		email  = fb.get('/Tech-Tailor/{}'.format(i),'Email')
		gender = fb.get('/Tech-Tailor/{}'.format(i),'Gender')
		phone = fb.get('/Tech-Tailor/{}'.format(i),'Phone Number')
		c.execute('''INSERT INTO `1` VALUES(?,?,?,?)''',(name,email,gender,phone))
		conn.commit()
	print("New Database count is being updated!!")
	new_count_file = open("count.txt","w")
	new_count = str(count-1)
	new_count_file.write(new_count)
	new_count_file.close()
	print("Data Uploaded to SQL Successfully!!")


if(__name__=="__main__"):
	

	count_file = open("count.txt","r")
	Saved_Count = count_file.read()
	Saved_Count = int(Saved_Count)

	if(Saved_Count == (count-1)):
		print("The Database is not updated!!")
		pass
	else:
		print("The Database has been updated!!!")
		print("New Data has started to Update to SQL!!")
		conn , c = create_sql()	
		import_and_write(conn,c)
#print(count-1)
