""" 
Controls all push functions to the database
Isaac
"""
from pymongo import MongoClient
from .basic import get_collection
import certifi
import time

def current_user():
	# Returns id of the current user from resources/id.txt
	with open("../resources/id.txt", "r") as r:
		return r.readline()

def push_to_db(user):
	# Pushes the user to the database with a unique id
	user["_id"] = str(time.time())
	user["matches"] = []
	user["likedby"] = []
	get_collection().insert_one(user)
	# This is a relative path and may cause issues later
	with open("resources/id.txt", "w") as w:
		w.write(user["_id"])
	return user
	
def push_like_to(user_id):
	# Pushes the current user to the given user's LikedBy list
	query = {"_id": user_id}
	newvalue = {"$push": {"likedby": current_user()}}
	get_collection().update_one(query, newvalue)
