from collections import Counter, defaultdict

wordlist = ['red', 'yellow', 'blue', 'red', 'green', 'blue', 'blue', 'yellow']

# invert a temporary Counter(wordlist) dictionary so keys are
# frequency of occurrence and values are lists the words encountered
freqword = defaultdict(list)
for word, freq in Counter(wordlist).items():
    freqword[freq].append(word)

# print in order of occurrence (with sorted list of words)
for freq in sorted(freqword):
    print('count {}: {}'.format(freq, sorted(freqword[freq])))