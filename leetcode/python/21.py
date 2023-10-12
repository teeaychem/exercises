# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# This looks to be on the faster side...

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
	if list1 == None:
		return list2
	if list2 == None:
		return list1
	if list1.val < list2.val:
		head = list1
		list1 = list1.next
	else:
		head = list2
		list2 = list2.next

	current = head

	while list1 != None and list2 != None:
		if list1.val < list2.val:
			current.next = list1
			current = list1
			list1 = list1.next
		else:
			current.next = list2
			current = list2
			list2 = list2.next

	if list1 != None:
		current.next = list1
	elif list2 != None:
		current.next = list2

	return head

# Taking a peek at other solutions, I'm not sure why the above is faster than most.
# It seems creating an initial node is common.
# And, maybe this slows things down.

# Seems a recursive version might also be slower as no tail.