class Vehicle():
	def __init__(self, engine_type, **kwargs):
		self.engine_type = engine_type
		for i in kwargs.keys():


	class Car():
		def __init__(self, engine_type, car_category, **kwargs):
			super().__init__(engine_type,**kwargs))

	def my_sum(*args):   # 1 * for tuple and ** for a dictionary
		total = 0
		for i in args:
			total += i
		return total

	print "My Sum: ", my_sum(10, 20)
	print  "My Sum: ", my_sum(10, 30, 40, 50, 60, 80)


	def output(name, **kwargs):
		print "name: ", name
		for i in kwargs:       #also runs as kwargs.keys
			print i, ":", kwargs[i] 

	output("Anne", age = 24, gender = "F", loc = "NBO")