test = """abc def-ghi jkl abc
abc"""

def calculate_word_frequency(s):
    # Post: return a list of words ordered from the most
    # frequent to the least frequent

    words = s.split()
    freq  = {}
    for word in words:
        if freq.has_key(word):
            freq[word] += 1
        else:
            freq[word] = 1
    return sort(freq)

def sort(d):
    # Post: sort dictionary d into list of words ordered
    # from highest freq to lowest freq
    # eg: For {"the": 3, "a": 9, "abc": 2} should be
    # sorted into the following list ["a","the","abc"]

    #I have never used lambda's so I'm not sure this is correct
    return d.sort(cmp = lambda x,y: cmp(d[x],d[y]))

print calculate_word_frequency(test)