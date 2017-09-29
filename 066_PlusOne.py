#Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

#You may assume the integer do not contain any leading zero, except the number 0 itself.

#The digits are stored such that the most significant digit is at the head of the list.

class Solution(object):
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		
		# if list is empty
		# return none

		# last = list.pop() # take off last number

		# last += 1
		# if last > 9
		# last = 0

		# num = plusOne(list) + last

		# LOOP UNTIL DONE

		# continue from right to left if 9
		
		# eg. 9799 --> 979[0] --> 97[0]0 --> 9[8]00
