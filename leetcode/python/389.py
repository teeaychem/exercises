# You are given two strings s and t.

# String t is generated by random shuffling string s and then add one more letter at a random position.

# Return the letter that was added to t.

# Example 1:

# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.
# Example 2:

# Input: s = "", t = "y"
# Output: "y"

# There are at least two ways to go here.
# 1. We can sort the two lists, and then find the first difference.
# 2. We can create a store of the characters in s and then finding any character in t either outside the store, or with a greater count than in the store.

def findTheDifferenceOne(s: str, t: str) -> str:

	s0 = sorted(s)
	t0 = sorted(t)

	for i in range(0, len(s)):
		if s0[i] != t0[i]:
			return t0[i]
	return t0[-1]

print(findTheDifferenceOne("", "y"))
print(findTheDifferenceOne("abcd", "abcde"))

def findTheDifferenceTwo(s: str, t: str) -> str:

	countDict = {}

	for i in range(0, len(s)):
		if countDict.get(s[i]) == None:
			countDict[s[i]] = 1
		else:
			countDict[s[i]] += 1
	for i in range(0, len(t)):
		if countDict.get(t[i]) == None:
			return t[i]
		elif countDict[t[i]] == 0:
			return t[i]
		else:
			countDict[t[i]] -= 1

print(findTheDifferenceTwo("", "y"))
print(findTheDifferenceTwo("abcd", "abcde"))