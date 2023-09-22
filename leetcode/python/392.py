# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false


# Idea is to work through the main string, keeping a pointer to where in the substring a match has been found for.
# If there's a match, either return True when all of the substring has been seen.
# Or, extend the pointer by one.
# Anything other than a match is ignored unless it's the starting char of the substring.
# In this case, the starting char was not an addition char in the string, so a new attempt should be made.


def isSubstring(s, t):

	position = 0

	if len(s) == 0:
		return True

	for i in range(0, len(t)):
		if t[i] == s[position]:
			if position == len(s) - 1:
				return True
			else:
				position += 1
		elif t[i] == s[0]:
			position = 1

	return False

print(isSubstring("abc", "baba"))
print(isSubstring("ab", "baab"))