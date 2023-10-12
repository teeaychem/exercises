# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


def strStr(haystack: str, needle: str) -> int:
	for i in range(0, len(haystack)):
		if haystack[i] == needle[0]:
			j = i
			k = 0
			while (k < len(needle) and j < len(haystack) and haystack[j] == needle[k]):
				j += 1
				k += 1
			if (k == len(needle)):
				return i
	return -1

print(strStr(haystack="sadbutsad", needle="sad"))
print(strStr(haystack="leetcode", needle="leeto"))
print(strStr(haystack="leetcocode", needle="code"))
print(strStr(haystack="hello", needle="ll"))

# This is slow, though
# The issue is we need to start a check from every viable starting point in haystack.
# We can't progress after a failed check as part of the failed check may be the initial part of a good result.
# E.g. haystack="cocode", needle="code".
# Wait, do you?
# Yes
# E.g. haystack="sssd", needle="ssd".
# If check after "ss" only "sd" remains.

# The following should be faster.
# The idea is to store the first possible starting point of needle skipped and then jump back.

def strStr2(haystack: str, needle: str) -> int:
	r = -1
	for i in range(0, len(haystack)):
		if haystack[i] == needle[0]:
			k = 0
			s = i
			while (k < len(needle) and i < len(haystack) and haystack[i] == needle[k]):
				if haystack[i] == needle[0] and r < 0:
					r = i
				i += 1
				k += 1
			if (k == len(needle)):
				return s
			elif r != -1:
				i = r

	return -1

print(strStr2(haystack="sadbutsad", needle="sad"))
print(strStr2(haystack="leetcode", needle="leeto"))
print(strStr2(haystack="leetcocode", needle="code"))
print(strStr2(haystack="hello", needle="ll"))

# Though, maybe this should be a for loop rather than a while loop. 
# I'm not sure what the interpreter does.