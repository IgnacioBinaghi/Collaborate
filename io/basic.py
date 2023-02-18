"""
This file provides basic operations for getting the database and collection
Isaac
"""
from pymongo import MongoClient
import certifi


def get_database():
   # Gets the database containing the collection of users
    ca = certifi.where()
    client = MongoClient("mongodb+srv://isaacfisher:9yqMyqfX1AlJ2p5x@collaborate.szhuyon.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
    return client['collaborate']

def get_collection():
   # Gets the collection to push users to
   dbname = get_database()
   collection_name = dbname["users"]
   return collection_name