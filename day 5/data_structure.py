#phone book

#  (1) Use a list

class PhoneBookList(object):
	''' 
	This class employs 'list' datastructure in managing phone contacts
	'''

	def __init__(self):
		self.book = []

	def add_contact(self, username, phone_number):
		record = [username, phone_number]
		self.book.append(record)

	def search(self, username):
		'''
		Returna a 'dict' with phone number and number of loop count e.g 
		{"username": "Annie", "phone_number": "93973597302"}
		'''
		count = 0

		for u, p in self.book:
			count += 1
			if u == username:
				result = {
						"count" : count,
						"phone_number" : p
						}
				return result

		result = {
				"count" : count,
				"phone_number" : None
				}


class PhoneBookDict(object):
	'''
	This class employs 'list' datastructure in managingphone contacts
	'''

	def __init__(self):
		self.book = {}

	def add_contact(self, username, phone_number):
		self.book[username] = phone_number
		#self.book['username']
		#

	def search(username, phone_number):
		result = {
			"count" : 1,
			"phone_number" : self.book.get(username, None)
				}
		
