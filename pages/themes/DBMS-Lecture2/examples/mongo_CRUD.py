import pymongo

# ------------------------- Connect to MongoDB Server ------------------------ #
# connect to MongoDB server:
client = pymongo.MongoClient("mongodb://localhost:27017")

# ----------------------- Switch context to a database ----------------------- #
# get "python_course" database:
db = client.python_course

# ------------------- Show all Collections in the database: ------------------ #
# get all collections in the database:
collections = db.list_collection_names()
# print(collections)

# ---------------------------------- Create ---------------------------------- #
# insert a new document into "todos" collection:
res = db.todos.insert_one({"title": "Learn MongoDB", "done": False})
# get the id of the inserted document:
# print(res.inserted_id)

# insert multiple documents into "todos" collection:
res = db.todos.insert_many([
	{"title": "Learn Python", "done": True},
	{"title": "Learn Flask", "done": False},
	{"title": "Learn Flask-MongoDB", "done": False}
])
# print(res.inserted_ids)

# insert multiple documents with different shape into "todos" collection:
res = db.todos.insert_many([
	{"title": "Learn Python", "done": True},
	{"title": "Learn Flask", "description":"Learn Flask to develop quick and easy web applications with the ability to scale up."},
	{"title": "Learn MongoDB", "due": "2021-12-31"}
])
# print(list(db.todos.find())[-3:-1])


# ----------------------------------- Read ----------------------------------- #
# find first document in "todos" collection:
print(db.todos.find_one())

# find all documents in "todos" collection:
for todo in db.todos.find():
	print(todo)