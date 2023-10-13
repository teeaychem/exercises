# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:

# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# The simplest soluton I can think of.
# Basically, continually skip over any node which matches the current node.
# As the nodes are sorted, this for sure removes all duplicates.

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
	node = head
	while (node != None):
		while (node.next != None and node.next.val == node.val):
			node.next = node.next.next
		node = node.next
	return head