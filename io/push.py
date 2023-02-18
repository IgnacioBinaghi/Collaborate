# Controls all push functions to the database
from pymongo import MongoClient
from basic import get_collection
import certifi



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