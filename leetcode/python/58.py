# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

# Approach is fairly simple.
# lwl is last word length.
# If a word is in progress, the previous index pointed to a character.
# And, if a word has started the previous index was a space.
# These are the two cases lwl is increased.
# Anything else is a space and is passed over.

def lengthOfLastWord(s: str) -> int:
	lwl = 0
	if (len(s) > 0 and s[0] != ' '):
		lwl = 1

	for i in range(1,len(s)):
		if s[i] != ' ':
			if s[i-1] != ' ':
				lwl += 1
			else:
				lwl = 1
	return lwl

print(lengthOfLastWord(s="   fly me   to   the moon  "))
print(lengthOfLastWord(s="luffy is still joyboy"))