"""Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

def addBinary(a: str, b: str) -> str:
	"""
	Given two binary strings, return their sum (also a binary string).
	Input strings are both non-empty and contains only characters 1 or 0.

	>>> addBinary("1", "0")
	'1'
	>>> addBinary("11", "1")
	'100'
	>>> addBinary("1010", "1011")
	'10101'
	"""
	# Base Case

	if len(a) < len(b):
		a, b = b, a

	if len(a) == 0:
		return ""
	# Recursive

	# return addBinary(b, "")
	if b == "":
		if len(a) > 1:
			rem = int(a[-1])
		elif len(a) == 1:
			rem = int(a[0])
	elif len(b) == 1:
		if len(a) > 1:
			rem = int(a[-1]) + int(b[0])
		elif len(a) == 1:
			rem = int(a[0]) + int(b[0])
	else:
		rem = int(a[-1]) + int(b[-1])

	if rem <= 1:
		return addBinary(a[:-1], b[:-1]) + str(rem)
	elif rem == 2:
		if len(a) > 1:
			new_a = a[:-2] + str(int(a[-2]) + 1)
			return addBinary(new_a, b[:-1]) + "0"
		else:
			return "10"


if __name__ == "__main__":
	import doctest
	doctest.testmod()
	print("*" * 20)
	print("doctests: done")
	print("*" * 20)
