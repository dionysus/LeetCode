def isPalindrome (s):
	
	while len(s) > 1:

		i = 0
		n = -1

		while not s[i].isalnum():
			i += 1

		while not s[n].isalnum():
			n -= 1

		if s[i].lower() != s[n].lower():
			return False

		else:
			s = s[i+1:n]

	return True


s = 'A man, a plan, a canal: Panama' 

print isPalindrome(s)
