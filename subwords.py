def subwords(word):
	""" return a set of all the words that compose the string word (parameter) 
	(e.g. subwords("hello") = set(['h', 'e', 'l', 'o', 'he', 'el', 'll', 'lo', 'hel', 'ell', 'llo', 'hell', 'ello', 'hello'])"""
	
	# we add each letters (no duplicates)
	all_words = set(word)
	
	# we add the 2 characters long and longer strings (no duplicates)
	for j in range(2,len(word)+1):
		for i in range(0,len(word)):
			all_words.add(word[i:j+i])

	return all_words

print subwords("hello")
print subwords("bonjour")
print subwords("ananas")
