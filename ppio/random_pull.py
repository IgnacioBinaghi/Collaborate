# A generator that will return the next random user
from .basic import get_collection
from random import shuffle
import json



def refresh_rand_list():
	random_user_list = get_collection().distinct("_id")
	shuffle(random_user_list)

	data = {
		"index" : len(random_user_list) - 1,
		"IDList" : random_user_list
	}

	with open("resources/rand.json", "w") as w:
		json.dump(data, w, indent=4)


def next_rand_user():
	with open("resources/rand.json", "r") as r:
		data = json.load(r)
		if data["index"] == 0:
			refresh_rand_list()
			return next_rand_user()
		result = data["IDList"][data["index"]]

	data["index"] -= 1

	with open("resources/rand.json", "w") as w:
		json.dump(data, w, indent=4)

	return result