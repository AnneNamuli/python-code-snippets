def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRUCTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" %(a, b)
	return a /b

print "Let's do some math with just functions!"

age = add(23, 45)
height = subtract(54, 12)
weight = multiply(21, 89)
iq = divide(250, 5)

print "Age: %d, Height: %d, Weight: %d, IQ: %d," %(age, height, weight,iq)

print "Here is a puzzle.."

what = add(age, subtract(height, multiply(weight,divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"