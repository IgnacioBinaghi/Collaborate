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
	with open("resources/id.txt", "r") as r:
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

def push_match_to(user_id):
	# Pushes the current user to the current and given user's matches list
	curr_user = current_user()
	collection = get_collection()
	query = {"_id": user_id}
	newvalue = {"$push": {"matches": curr_user}}
	collection.update_one(query, newvalue)
	query = {"_id": curr_user}
	newvalue = {"$push": {"matches": user_id}}
	collection.update_one(query, newvalue)

def update_courses(courses):
	# Pushes the courses to the currents users course string
	query = {"_id": current_user()}
	newvalue = {"$push": {"courses": courses}}
	get_collection().update_one(query, newvalue)

def update_topics(topics):
	# Pushes the topics to the current user's topics string
	query = {"_id": current_user()}
	newvalue = {"$push": {"topics": topics}}
	get_collection().update_one(query, newvalue)

def update_area(area):
	# Pushes the area to the given user's area string
	query = {"_id": current_user()}
	newvalue = {"$push": {"Area": area}}
	get_collection().update_one(query, newvalue)

def update_bio(bio):
	# Pushes the bio to the given user's bio string
	query = {"_id": current_user()}
	newvalue = {"$push": {"bio": bio}}
	get_collection().update_one(query, newvalue)

def update_insta(insta):
	# Pushes the current user to the given user's LikedBy list
	query = {"_id": current_user()}
	newvalue = {"$push": {"socials": insta}}
	get_collection().update_one(query, newvalue)
