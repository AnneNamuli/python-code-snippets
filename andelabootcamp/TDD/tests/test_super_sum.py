import unittest

from mathx.super_sum import super_sum

class SuperSumtest(unittest.TestCase):
	def test_two_numbers(self):
		result = super_sum(20, 20)
		self.assertEqual(result, 40)

	def test_four_numbers(self):
		result = super_sum(10, 30, 50, 20)
		self.assertEqual(result, 110)

	def test_two_lists(self):
		a = [10, 20, 30, 40]
		b = [100, 20]
		result = super_sum(a, b)
		self.assertEqual(result, 220)

	def test_list_and_number(self):
		a = [10, 30, 50]
		result = super_sum(a, 50)
		self.assertEqual(result, 140)

	def test_four_lists(self):
		a, b, c, d =[1, 2], [2, 3], [3], [4, 10]
		result = super_sum(a, b, c, d)
		self.assertEqual