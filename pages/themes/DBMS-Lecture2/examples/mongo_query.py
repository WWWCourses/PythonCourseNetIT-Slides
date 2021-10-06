import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.python_course


# find all documents in "todos" which are completed and "priority" is greater than or equal to 2
# todos = db.todos.find({"$and":[
# 	{"completed":True},
# 	{"priority":{"$gte":2}}]
# })

# find all documents in "todos" with due date in the past
todos = db.todos.find({"dueDate":{"$lt":datetime.now()}})

for todo in todos:
	print(todo)
