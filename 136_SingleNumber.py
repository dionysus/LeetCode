def singleNumber(nums):

	if len(nums) == 1:
		return nums[0]

	match = nums[1:].index(nums[0])
	if match == -1:
		return nums[0]
	else:
		del nums[match]
		return singleNumber(nums[1:])

list = [2,2,3,3,1,1,4]
print singleNumber(list)