class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
	symbols = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	combos = {'V':'I', 'X':'I', 'L':'X', 'C':'X', 'D':'C', 'M':'C'}

	letters = []

	sum = 0

	for letter in s:
		letters.append(letter)

	while True:

		if letters:
			case = letters.pop()

			if letters and case in combos and letters[-1] == combos[case]:
				comboletter = letters.pop()
				sum = sum + symbols[case] - symbols[comboletter]
			else:
				sum += symbols[case]
		else:
			break

	return sum        