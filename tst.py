test = "one fish two fish red fish blue fish"
def words(phrase):
    wordlist = phrase.split()
    freq  = {}
    for word in wordlist:
      
        try:
            word = int(word)
            if freq.has_key(word):
                freq[word] += 1
            else:
                freq[word] = 1
        except ValueError:
            if freq.has_key(word):
                freq[word] += 1
            else:
                freq[word] = 1
    return freq
print(words(test))