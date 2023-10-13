# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

# Is there a more elegant way of doing this?
# The copy of nums1 could be avoided by shifting every element to the end of nums1.
# This is fine as either an element gets shifted forward or every element of nums2 comes before any element of nums1.
# Conceptually it's fine.
# But, is there a clearer expression?
# C would be nice for inlining incrementation.

def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:
	"""
	Do not return anything, modify nums1 in-place instead.
	"""
	p1 = 0
	p2 = 0
	nums1c = nums1[:m]
	while p1 < m and p2 < n:
		if nums1c[p1] == nums2[p2]:
			nums1[p1 + p2] = nums2[p2]
			nums1[p1 + p2 + 1] = nums2[p2]
			p1 += 1
			p2 += 1
		elif nums1c[p1] < nums2[p2]:
			nums1[p1 + p2] = nums1c[p1]
			p1 += 1
		else: 
			nums1[p1 + p2] = nums2[p2]
			p2 += 1
	while p1 < m:
		nums1[p1 + p2] = nums1c[p1]
		p1 += 1
	while p2 < n:
		nums1[p1 + p2] = nums2[p2]
		p2 += 1

x1 = [1,2,3,0,0,0]
y1 = [2,5,6]
merge(nums1=x1, m=3, nums2=y1, n=3)
print(x1)