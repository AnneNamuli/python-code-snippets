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

book1 = PhoneBookList()

book1.add_contact("Annie", "09981791384")
book1.add_contact("Sammy", "8908247345")
book1.add_contact("Rachel", "90374973874")
book1.add_contact("Dannie", "798340074320")
book1.add_contact("Dennis", "79340290348")
book1.add_contact("Anthony", "87209384134")

print book1.book


#lets search
print book1.search("Sammy")
print book1.search("Annie")
print book1.search("Margreth")


