# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# This is kind of simple, in that it's just a lookup table.
# Though, I feel there should be a cleaner way of doing this.
# I guess using bit operators would clean things up.
# And, the last elif and else should be merged in line with the first two cases.

def addBinary(a: str, b: str) -> str:
	# add trailing 0s to shortest if needed
	carry = 0
	if len(a) < len(b):
		a = (len(b) - len(a)) * "0" + a
	elif len(b) < len(a):
		b = (len(a) - len(b)) * "0" + b
	
	result = ""

	# go backwards and basically do a lookup table.
	for i in range(len(a) - 1, -1, -1):
		if a[i] == b[i] == "1":
			if carry:
				result = "1" + result
			else:
				result = "0" + result
			carry = 1
		elif a[i] != b[i]:
			if carry > 0:
				result = "0" + result
			else:
				result = "1" + result
		elif carry > 0:
			result = "1" + result
			carry = 0
		else:
			result = "0" + result
	if carry > 0:
		result = "1" + result
	return result

print(addBinary(a="101", b="1"))
print(addBinary(a="1010", b="1011"))
print(addBinary(a="11", b="1"))
print(addBinary(a="1111", b="1111"))