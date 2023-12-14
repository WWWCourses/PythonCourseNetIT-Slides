from pymongo import MongoClient
from bson import encode, Int64

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["test"]
collection = db["coll1"]

# Insert a document with a 32 and 64 bit integers
collection.insert_one({
	"exampleInt32": 12345,
	"exampleInt64": Int64(12345),
	"name":"Ada"
})

# Retrieve the document
document = collection.find_one({"exampleInt64": 12345})
print(document)

# Serialize the field value to BSON and check its length
field_32 = encode({"exampleInt32": document["exampleInt32"]})
field_64 = encode({"exampleInt64": document["exampleInt64"]})

print(f"Size of 'exampleInt32' field in bytes: {len(field_32)}")
print(f"Size of 'exampleInt64' field in bytes: {len(field_64)}")



