from data_structure import PhoneBookList, PhoneBookDict
book1 = PhoneBookList()

book1.add_contact("Annie", "09981791384")
book1.add_contact("Sammy", "8908247345")
book1.add_contact("Rachel", "90374973874")
book1.add_contact("Dannie", "798340074320")
book1.add_contact("Dennis", "79340290348")
book1.add_contact("Anthony", "87209384134")

print book1.book


#lets search
print "Sammy: ", book1.search("Sammy")
print "Annie: ", book1.search("Annie")
print "Margreth: ", book1.search("Margreth")

# Printing the phonebooklist
book2 = PhoneBookDict()

book1.add_contact("Annie", "09981791384")
book1.add_contact("Sammy", "8908247345")
book1.add_contact("Rachel", "90374973874")
book1.add_contact("Dannie", "798340074320")
book1.add_contact("Dennis", "79340290348")
book1.add_contact("Anthony", "87209384134")

print book2.book


#lets search
print "Sammy: ", book2.search("Sammy")
print "Annie: ", book2.search("Annie")
print "Margreth: ", book2.search("Margreth")




