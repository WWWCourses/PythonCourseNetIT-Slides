# db/operations.py

from pymongo import MongoClient
from bson.objectid import ObjectId
from .config import db_config

class MongoDB:
    def __init__(self):
        self.client = MongoClient(db_config['uri'])
        self.db = self.client[db_config['database']]
        self.collection = self.db[db_config['collection']]

    def create_user(self, name, email):
        user = {'name': name, 'email': email}
        self.collection.insert_one(user)
        print("User created successfully")

    def get_users(self):
        users = self.collection.find()
        for user in users:
            print(user)

    def update_user_email(self, user_id, new_email):
        self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': {'email': new_email}})
        print("User email updated successfully")

    def delete_user(self, user_id):
        self.collection.delete_one({'_id': ObjectId(user_id)})
        print("User deleted successfully")
