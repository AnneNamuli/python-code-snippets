the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "strawberries", "plums"]
change = [1, "pennies", 2, "dimes", 3, "quarters", 4, "shillings"]

for number in the_count:
	print "\n"
	print "\tThis is count %d" % number

for fruit in fruits:
	print "\n"
	print "\tA fruit of type: %s" % fruit

for i in change:
	print "\n"
	print "\tI got %r" % i

elements = []

for i in range(0, 6):
	print "\n"
	print "\tAdding %d to the list " % i

	elements.append(i)

for i in elements:
	print "\n"
	print "\tElements was: %d" % i

