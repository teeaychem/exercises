# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

# Example 1:

# Input: s = "aab"
# Output: 0
# Explanation: s is already good.
# Example 2:

# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
# Example 3:

# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

# Constraints:

# 1 <= s.length <= 105
# s contains only lowercase English letters.

class Solution:
	def minDeletions(s: str):
		
		charFreq = [0] * 26
		for char in s:
				charFreq[ord(char) - ord('a')] += 1

		removed = 0
		uniqueFreq = set()
		
		for i in range(0,26):
			freq = charFreq[i]
			while (freq in uniqueFreq) and freq > 0:
				removed += 1
				freq -= 1
			uniqueFreq.add(freq)

		return removed

print(Solution.minDeletions("abcdefgzz"))
print(Solution.minDeletions("abb"))
print(Solution.minDeletions("aabb"))
print(Solution.minDeletions("aaabbbcc"))

# Simple solution.
# Count the frequency of each character.
# Then, keep subtracting from the frequencies until they're unique.
# Apparently this is kind of slow.
# Like, things can be done twice as fast.
# Some other time...