def reverse(s):
	s = list(s)
	for i in range (len(s)//2):
		temp  = s[i]
		s[i] = s[len(s)- i -1]
		s[len(s) - 1 - i] = temp

	return "".join(s)

print reverse("hello")
