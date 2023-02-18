from pymongo import MongoClient
import basic
import certifi


db = basic.get_database()
collection = basic.get_collection()


def haveLikedBy(userID):
    user = collection.find_one({"_id" : str(userID)})
    userLikedByList = user.get("likedby")
    if (len(userLikedByList) == 0) :
        return False
    else :
        return True

def pullLikedBy(userID):
    user = collection.find_one({"_id" : str(userID)})
    userLikedByList = user.get("likedby")
    lastElement = userLikedByList[len(userLikedByList)-1]
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
