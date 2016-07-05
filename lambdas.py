def add(x, y):
	return x + y

#lambda function

y = lambda x, y : x + y
print add(10, 2)

print y(12, 5)

def make_incrementor(n):
	return lambda x: x + n

z = make_incrementor(10)

print z

# filter out n | n % 2 == 0
def is_even(n):
	return n % 2 == 0 # always returns true or false.. no need for is statement

l = [2, 19, 4, 34, 29, 6, 12]
new_list = filter(is_even, l)

print new_list
