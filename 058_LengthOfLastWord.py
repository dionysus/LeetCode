def lengthOfLastWord(s):

	i = 0
	
	if len(s) > 0:
		while s[-(i+1)] != ' ':
			i += 1
	
	return i

print lengthOfLastWord("")