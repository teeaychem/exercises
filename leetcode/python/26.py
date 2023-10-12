# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# As simple as possible.
# Guaranteed nums has one element and is sorted, so start with the elem and collect
# all unique elems by comparison with last already found.
# Then, overwrite initial k elems with unique.

def removeDuplicates(nums: [int]) -> int:

	unique = [nums[0]]

	for i in range(1,len(nums)):
		if nums[i] != unique[len(unique) - 1]:
			unique.append(nums[i])


	for i in range(0, len(unique)):
		nums[i] = unique[i]

	return len(unique)

nums=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums=nums))
print(nums)
print(removeDuplicates(nums=[1,1,2]))

# Preferred version keeps two inidices.
# First to current unique, other to how many duplicates have been seen.
# This allows updating in place without an additional list.

def removeDuplicates(nums: [int]) -> int:

	k = 0
	l =0
	length = len(nums)

	while ((k + l) < length):
		if nums[k] == nums[k + l]:
			l += 1
		else:
			nums[k + 1] = nums[k + l]
			k += 1

	return k + 1

nums=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums=nums))
print(nums)
print(removeDuplicates(nums=[1,1,2]))

# For some reason the second comes out slower on leetcode.
# My guess is this is due to load.
# Else, the compiler is up to something interesting!