# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# Basically, create a stack to store open (left) parantheses.
# Every time a left paranthesis is found, put it on the stack.
# Every time a right paranthesis is found, take the first paranthesis off the stack and check for a match.
# At the end check there's no left parantheses left over.

# This was a cool problem. I'd wondered about how this was done, and when pushed to think at least one fairly simple solution came to mind.

def isValid(s: str) -> bool:
	stack = []

	for i in range(0, len(s)):
		if s[i] in ["(", "{", "["]:
			stack.append(s[i])
		elif len(stack) == 0:
			return False
		else:
			l = stack.pop()
			if l == "(" and s[i]!= ")":
				return False
			elif l == "{" and s[i]!= "}":
				return False
			if l == "[" and s[i]!= "]":
				return False
	if len(stack) == 0:
		return True
	else:
		return False

print(isValid(s="()"))
print(isValid(s="()}"))
print(isValid(s="()[]{}"))
print(isValid(s="(]"))