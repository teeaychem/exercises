# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1

def singleNumber(nums: [int]):
	seenSet = set()
	for i in range(0, len(nums)):
		if nums[i] in seenSet:
			seenSet.remove(nums[i])
		else:
			seenSet.add(nums[i])

	return seenSet.pop()

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))

# Unless compiler is doing something interesting, this should be a little faster

def singleNumber2(nums: [int]):
	val = 0
	seenSet = set()
	for i in range(0, len(nums)):
		if nums[i] in seenSet:
			val -= nums[i]
		else:
			seenSet.add(nums[i])
			val += nums[i]

	return val

print(singleNumber2([2,2,1]))
print(singleNumber2([4,1,2,1,2]))
print(singleNumber2([1]))