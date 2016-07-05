def num_to_words2(n):
	words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
	if n <= 9:
		return words[n]

	else:
		return num_to_words2(n//10) + "" + words[n%10]
 