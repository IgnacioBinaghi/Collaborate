# A generator that will return the next random user
from .basic import get_collection
from random import shuffle

class random_users(object):

	random_user_list = []

	def __init__(self):
		self.random_user_list = get_collection().distinct("_id")
		shuffle(self.random_user_list)

	def __iter__(self):
		return self

	def __next__(self):
		return self.next()

	def next(self):
		if (len(self.random_user_list) == 0):
			self.random_user_list = get_collection().distinct("_id")
			shuffle(self.random_user_list)

		res = self.random_user_list[0]
		self.random_user_list = self.random_user_list[1:]
		return res