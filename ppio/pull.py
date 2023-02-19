
# Controlls all pull functions in the database
from .basic import get_collection

def login(username, password):
	user = get_collection().find_one({"user": username})
	if (user == None):
		return False
	if (user["pass"] != password):	
		return False
	else:
		with open("resources/id.txt", "w") as w:
			w.write(user["_id"])
		return True

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
	get_collection().update_one(myquery, newvalues)
	# lastElement = 
	return lastElement

def get_user(id):
	return get_collection().find_one({"_id": id})