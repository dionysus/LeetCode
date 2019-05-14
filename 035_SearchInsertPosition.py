from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    """
    >>> searchInsert([1,3,5,6], 5)
    2
    >>> searchInsert([1,3,5,6], 2)
    1
    >>> searchInsert([1,3,5,6], 7)
    4
    >>> searchInsert([1,3,5,6], 0)
    0
    """
    if nums == []:
        return 0

    for i in range(len(nums)):
        if target <= nums[i]:
            return i

    return len(nums)
