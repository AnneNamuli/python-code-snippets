def sqr(n):
	for i in range(n):
		return i ** 2

# using lambda
f = lambda s, e: [i * i for i in range(s, e + 1)]
print f(2, 40)