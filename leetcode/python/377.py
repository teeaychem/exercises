# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:

# Input: nums = [9], target = 3
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
 

# Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:



memo = [0]

def basic(list, n):	
	if n == 0:
		return 1
	elif n < 0:
		return 0
	else:
		sum = 0
		for i in range(0, len(list)):
				sum += basic(list, n - list[i])
	return sum

# Work up to the target where each n is treated as a target.
# For each n, the number of ways to make n is obtained by examining the list.
# For each element, we check n - that element.
# If this is 0, we have a new way of getting the target together with all the ways of getting to the other value.
# Otherwise, we just have an alternative way of getting to the other value.

def memo(list, n):
	listLength = len(list)
	memo = []
	for i in range(0,n+1):
		total = 0
		for j in range(0,listLength):
			if i - list[j] == 0:
				total += 1 + memo[i - list[j]]
			elif i - list[j] > 0:
				total += memo[i - list[j]]
		memo.append(total)
	return memo[n]


print(basic([1,2,3], 3))
print(basic([1,2,3], 4))
print(basic([1,2,3], 5))
print(basic([1,2,3], 6))
# print(basic([9], 3))

print(memo([1,2,3], 3))
print(memo([1,2,3], 4))
print(memo([1,2,3], 5))
print(memo([1,2,3], 6))