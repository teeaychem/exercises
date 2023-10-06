# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# I guess a very standard solution.
# There's at least one string guaranteed, so use this as a base.
# Only thing of note is using min to ensure check stays in bound and doing this before the check as "and" is evaled left to right.

def longestCommonPrefix(strs: [str]) -> str:

	lcp = strs[0]

	for i in range(1,len(strs)):
		a = 0
		b = min(len(lcp), len(strs[i])) # only do comparison once for each while loop
		while (a < b and lcp[a] == strs[i][a]):
			a += 1
		lcp = lcp[:a]
	return lcp

print(longestCommonPrefix(strs=["Hi", "Hithere"]))
print(longestCommonPrefix(strs=["flower","flow","flight"]))
print(longestCommonPrefix(strs=["dog","racecar","car"]))