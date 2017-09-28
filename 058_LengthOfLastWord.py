def lengthOfLastWord(s):
	
	def length(n):
		sum = 0

		if len(n) < 1 or n[-1] == ' ':
			return sum

		if n[-1] != ' ':
			sum += 1
		
		return sum + length(n[:-1])

	if len(s) < 1:
			return 0

	while s[-1] == ' ':
		s = s[:-1]

	return length(s)

print lengthOfLastWord('  ')