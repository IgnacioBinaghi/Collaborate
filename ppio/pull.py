from pymongo import MongoClient
from .basic import get_collection
import certifi


def have_liked_by():
	with open("resources/id.txt", "r") as r:
		userID = r.readline()
	user = get_collection().find_one({"_id" : userID})
	userLikedByList = user.get("likedby")
	if (len(userLikedByList) == 0) :
		return False
	else :
		return True

def pull_liked_by():
	with open("resources/id.txt", "r") as r:
		userID = r.readline()
	user = get_collection().find_one({"_id" : str(userID)})
	userLikedByList = user.get("likedby")
	lastElement = userLikedByList[-1]
	userLikedByList.pop()
	print(userLikedByList)
	print(type(userLikedByList))
	myquery = {"_id" : str(userID)}
	newvalues = { "$set" : {"likedby" : userLikedByList}}
	collection.update_one(myquery, newvalues)
	# lastElement = 
	return lastElement





# newvalues = { "$set": { "address": "Canyon 123" } }
# mycol.update_one(myquery, newvalues)
