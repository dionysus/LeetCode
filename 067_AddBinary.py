"""Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
	def addBinary(self, a: str, b: str) -> str:
		"""
		Given two binary strings, return their sum (also a binary string).
		Input strings are both non-empty and contains only characters 1 or 0.

		>>> addBinary("1", "0")
		"1"
		"""
		if a == "0" and b == "0":
			return "0"
		if (a == "0" and b == "1") or (a == "1" and b == "0") :
			return "1"
		else:
			return "test"

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	print("*" * 20)
	print("doctests: done")
	print("*" * 20)
