""" 
Controls all push functions to the database
Isaac
"""
from pymongo import MongoClient
from basic import get_collection
import certifi
import time

def current_user():
	# Returns id of the current user from resources/id.txt
	with open("../resources/id.txt", "r") as r:
		return r.readline()

def push_to_db(user):
	# Pushes the user to the database with a unique id
	user["_id"] = str(time.time())
	get_collection().insert_one(user)
	with open("../resources/id.txt", "w") as w:
		w.write(user["_id"])
	return user
	
def push_like_to(user_id):
	# Pushes the current user to the given user's LikedBy list
	query = {"_id": user_id}
	newvalue = {"$push": {"likedby": current_user()}}
	get_collection().update_one(query, newvalue)

push_to_db({"ignacio": "binaghi"})
push_like_to("1")

"""
user_template = {
  "_id" : "1",
  "name" : "John Doe",
  "age" : "19",
  "year" : "2",
  "school" : "NYU",
  "socials" : ["twitter.com"],
  "Area" : ["Brooklyn", "Manhattan"],
  "courses": "CSO",
  "topics": "Calculus",
  "bio": "sex? pls",
  "user": "username",
  "pass": "password",
  "likedby": ["you"]
}
get_collection().insert_one(user_template)
"""