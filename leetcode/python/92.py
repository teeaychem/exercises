# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n

# Follow up: Could you do it in one pass?

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
class Solution:

	# reversing a list one pass.
	def reverseList(head: [ListNode]):

		# if no nodes, nothing to be done
		if head == None:
			return None

		# set up three pointers, to the past present and future nodes.
		past = None
		present = head
		future = None
		
		if present.next != None: # move forward by one if possible
			past = present
			present = present.next
			future = present.next
			past.next = None # erase past, as this is now end.
		else: # otherwise, just one node, so reverse is same
			return present
		
		# so long as there's additional nodes to consider, reverse the present node
		# then, shift everything forward.
		while present.next != None: 
			present.next = past
			past = present
			present = future
			future = present.next

		# final reverse, as while only reverses when there's a future node
		present.next = past

		return present

	# modification to reversing list in one pass to take a limit.
	# key idea is store the first node.
	# this first node becomes last in reversed list.
	# so, at the end, point the first node to the rest of the list
	def reverseListUntil(head: [ListNode], limit: int):
		print("reversing: " + listNodes(head))

		if limit == 0:
			return head

		count = 1 # used to stay within limit

		past = None # previous node
		present = head # current node
		future = None # future node

		if present == None:
			return None

		if present.next != None:
			past = present
			present = present.next
			future = present.next
		else:
			return present

		base = past # store initial node
		past.next = None
		
		while present.next != None and count < limit:
			present.next = past
			past = present
			present = future
			future = present.next
			count += 1

		present.next = past
		base.next = future
		
		return present

	# to reverse between to indicies, work through the list until first.
	# then, calculate limit to reverse until.
	def reverseBetween(head: [ListNode], left: int, right: int):

		present = head
		past = None

		if head == None or head.next == None:
			return head

		count = 1

		while count < left and present != None:
			past = present
			present = present.next
			count += 1

		present = Solution.reverseListUntil(head=present, limit=(right - left))
		if past != None:
			past.next = present
		else:
			head = present

		return head

def listNodes(nodes):
	pointer = nodes
	string = ""
	while pointer != None:
		string += ("%d," % pointer.val)
		pointer = pointer.next
	return "[%s]" % string[:-1]

test0 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
test1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
# printNodes(test)
# printNodes(Solution.reverseList(head=test))
print(listNodes(Solution.reverseBetween(head=test0, left=2, right=4))) # [1,4,3,2,5]
print(listNodes(Solution.reverseBetween(head=test1, left=2, right=3))) # [1,3,2,4,5,6]
print(listNodes(Solution.reverseBetween(head=ListNode(1, ListNode(2, None)), left=1, right=2))) # [2,1]
print(listNodes(Solution.reverseBetween(head=ListNode(5, None), left=1, right=1)))
print(listNodes(Solution.reverseBetween(head=ListNode(1, None), left=0, right=0)))
print(listNodes(Solution.reverseBetween(head=ListNode(3, ListNode(5, None)), left=1, right=1))) # [3,5]
print(listNodes(Solution.reverseBetween(head=ListNode(1, ListNode(2, ListNode(3, None))), left=3, right=3))) # [1,2,3]