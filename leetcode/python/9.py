# Given an integer x, return true if x is a  palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Constraints:

# -231 <= x <= 231 - 1

# Follow up: Could you solve it without converting the integer to a string?

# Standard approach (I guess).
# Only issue is getting reverse indexing right.

def isPalindrome(x: int) -> bool:
	s = str(x)
	for i in range(0,len(s)//2):
		if s[i] != s[- (i + 1)]:
			return False
	
	return True

print(isPalindrome(121))
print(isPalindrome(1001))
print(isPalindrome(-121))