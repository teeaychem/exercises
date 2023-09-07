# 725. Split Linked List in Parts
# Medium
# 3.4K
# 280
# Companies
# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

# Return an array of the k parts.

 

# Example 1:


# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode is [].
# Example 2:


# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
 

# Constraints:

# The number of nodes in the list is in the range [0, 1000].
# 0 <= Node.val <= 1000
# 1 <= k <= 50


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
class SolutionOne:
		def splitListToParts(head: [ListNode], k: int):
			count = 0
			pointer = head
			while pointer != None:
				count += 1
				pointer = pointer.next

			buckets = [0] * k
			for i in range(0,count):
					buckets[i % k] += 1

			pointer = head
			for i in range(0, k):
				if buckets[i] == 0:
					buckets[i] = None
				else:
					shift = buckets[i]
					buckets[i] = pointer
					while shift != 1:
						pointer = pointer.next
						shift -= 1
					# if pointer != None:
					temp = pointer.next
					pointer.next = None
					pointer = temp
		
			return buckets



# Hm, 

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
			count = 0
			pointer = head
			while pointer != None:
				count += 1
				pointer = pointer.next

			sublistMostCount = count // k
			sublistExtraCount = count % k

			buckets = [None] * k

			pointer = head
			for i in range(0, k):
				buckets[i] = pointer

				countto = sublistMostCount - 1
				if i < sublistExtraCount:
					countto += 1

				for j in range(0, countto):
					if pointer != None:
							pointer = pointer.next
				if pointer != None:
					temp = pointer.next
					pointer.next = None
					pointer = temp
			
			return buckets

thead = ListNode(1, ListNode(2, ListNode(3,None)))

print(Solution.splitListToParts(head=thead, k=5))

# head =
# [1,2,3,4,5,6,7,8,9,10]
# k =
# 3
# Output
# [[1,2,3,4],[5,6,7,8],[9,10]]
# Expected
# [[1,2,3,4],[5,6,7],[8,9,10]]

# To figure out the distribution, divide by k.
# if count > k then this is positive.
# if count < k this is negative, but then modulo is positive, so we'll end up with an even distribution.
# do -1 as we us this is the baseline.
# if there's imbalance, then everything left over is one less.