def lengthOfLastWord(s):
	
	sum = 0

	if len(s) < 1:
		return sum

	if s[-1] != ' ':
		sum += 1
		return sum + lengthOfLastWord(s[:-1])
	
	return sum

#n = ''
#print n[-1]
print lengthOfLastWord("")
print lengthOfLastWord("a")
print lengthOfLastWord("asdfs dfds")