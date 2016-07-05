def Words(word_input):
# word frequency in a text

	word_input = """Man who run in front of car, get tired.
	Man who run behind car, get exhausted."""

	print "Original string:"
	print word_input

	print

	# create a list of words separated at whitespaces
	wordList1 = word_input.split(None)

	# strip any punctuation marks and build modified word list
	# start with an empty list
	wordList2 = []
	for word1 in wordList1:
	    # last character of each word
	    lastchar = word1[-1:]
	    # use a list of punctuation marks
	    if lastchar in [",", ".", "!", "?", ";"]:
	        word2 = word1.rstrip(lastchar)
	    else:
	        word2 = word1
	    # build a wordList of lower case modified words
	    wordList2.append(word2.lower())

	print "Word list created from modified string:"
	print wordList2

	print

	# create a wordfrequency dictionary
	# start with an empty dictionary
	freqD2 = {}
	for word2 in wordList2:
	    freqD2[word2] = freqD2.get(word2, 0) + 1
	    
	# create a list of keys and sort the list
	# all words are lower case already
	keyList = freqD2.keys()
	keyList.sort()

	print "Frequency of each word in the word list (sorted):"
	for key2 in keyList:
	  print "%-10s %d" % (key2, freqD2[key2])

