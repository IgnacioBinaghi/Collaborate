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
