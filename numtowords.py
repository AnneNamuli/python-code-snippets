def num_to_words(n):
	nw = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "sevem", 8 : "eight", 9 : "nine" }
	n = str(n)
	for i in n:
		words.append(nw[i])

	return "".join(words)


	n = input("Please enter your number: ")
	
