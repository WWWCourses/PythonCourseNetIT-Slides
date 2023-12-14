import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.python_course

# print(dict(client.server_info()))
server_status = client.admin.command("serverStatus")
print(server_status["connections"])