import pyrebase

class iter_count:
	def __init__(self):
		config = {
			"apiKey": "AIzaSyAhusK8H900iMxt7k-IRqyIgmJASQkzhIc",
    		"authDomain": "image-db-d8b91.firebaseapp.com",
    		"databaseURL": "https://image-db-d8b91.firebaseio.com",
    		"projectId": "image-db-d8b91",
    		"storageBucket": "image-db-d8b91.appspot.com",
    		"messagingSenderId": "442834729478"}

		self.firebase = pyrebase.initialize_app(config)
	def get_count(self):
		db = self.firebase.database()
		count = 0
		count_all = 0
		for i in (db.child("Tech-Tailor").get().each()):
			if i.val() is not None:
				count+=1
			count_all+=1		
		return count,count_all
