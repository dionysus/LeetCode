def isPalindrome (s):
	
	newString = ''

	for i in s:
		if i.isalnum():
			if i.isalpha():
				newString += i.lower()
			else:
				newString += i

	for i in range (0, len(newString)/2):
		if newString[i] != newString[-(i+1)]:
			return False

	return True

s = 'A man, a plan, a canal: Panama! '
print isPalindrome(s)