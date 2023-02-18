# Controls all push functions to the database
from pymongo import MongoClient
import certifi


def get_database():

   ca = certifi.where()
   client = MongoClient("mongodb+srv://isaacfisher:9yqMyqfX1AlJ2p5x@collaborate.szhuyon.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['collaborate']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
   print(dbname)