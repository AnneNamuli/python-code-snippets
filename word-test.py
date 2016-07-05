def words(phrase):
  word_input = phrase.split(None)
  wordlist = [word_input]
  count = 0
  for word in wordlist:
    count = wordlist.count(word)
    # return count
  print(word + ": " + str(count))
    
words("olly olly in come free")