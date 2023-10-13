# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# So, a binary search.
# There's not much too this, other than a check on which value to return if the value is not found.
# As // gets floor, m will always be lower.
# halfway between u and l is distance between offset by l.
# i.e. m = (l + (u - l)//2)
# and m = (l + (u - l)//2) = (l + u//2 - l//2) = (l//2 + u//2) = ((u + l)//2)

def searchInsert(nums: [int], target: int) -> int:
	l = 0
	u = len(nums) - 1
	m = 0
	while u >= l:
		m = ((u + l) // 2)

		if nums[m] < target:
			l = m + 1
		elif nums[m] > target:
			u = m - 1
		elif nums[m] == target:
			return m
	if nums[m] < target:
		return m + 1
	else:
		return m

print(searchInsert(nums=[1,3,5,6], target=5))
print(searchInsert(nums=[1,3,5,6], target=2))
print(searchInsert(nums=[1,3,5,6], target=7))
print(searchInsert(nums=[1,3,5,6], target=0))