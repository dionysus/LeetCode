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
	"1"
	"""

	if len(a) == len(b) == "0":
		return ""
	else:
		if len(a) == 0:
			num_a = 0
		else:
			num_a = int(a[-1])
		if len(b) == 0:
			num_b = 0
		else:
			num_b = int(b[-1])

		num_c = num_a + num_b

		if num_c >= 2:
			if len(a) == 1:
				new_a = str(num_c - 1)
			else:
				new_a = a[0:-2] + str(int(a[-2]) + num_c - 1)
			return addBinary(new_a, b[:-1]) + "1"
		else:
			return addBinary(a[:-1], b[:-1]) + str(num_c)
	"""
	index of end
	add pair + carry over
	if greater than 1, carryover
	return single str
	"""


if __name__ == "__main__":
	import doctest
	doctest.testmod()
	print("*" * 20)
	print("doctests: done")
	print("*" * 20)
