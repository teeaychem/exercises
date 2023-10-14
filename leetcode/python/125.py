# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# Using built in isalnum/lower as unlike C I'm not sure how strings are represented in python (and the built is likely fastest in any case).
# Note, left < right rather than left != right as no guarantee left and right converge.

def isPalindrome(s: str) -> bool:
	left = 0
	right = len(s) - 1
	while (left < right):
		if s[left].isalnum() == False:
			left += 1
		elif s[right].isalnum() == False:
			right -= 1
		elif s[left].lower() == s[right].lower():
			left += 1
			right -= 1
		else:
			return False
	return True
