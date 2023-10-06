# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# A lookup table.
# This is nothing too interseting.

def romanToInt(s: str) -> int:

	n = 0

	for i in range(0, len(s)):
		if s[i] == "I":
			if i + 1 < len(s) and (s[i + 1] == "V" or s[i + 1] == "X"):
					n -= 1
			else:
				n += 1
		if s[i] == "V":
			n += 5
		if s[i] == "X":
			if i + 1 < len(s) and (s[i + 1] == "L" or s[i + 1] == "C"):
				n -= 10
			else:
				n += 10
		if s[i] == "L":
			n += 50
		if s[i] == "C":
			if i + 1 < len(s) and (s[i + 1] == "D" or s[i + 1] == "M"):
				n -= 100
			else:
				n += 100
		if s[i] == "D":
			n += 500
		if s[i] == "M":
			n += 1000

	return n

print(romanToInt(s="IV"))
print(romanToInt(s="XXVII"))
print(romanToInt(s="CIX"))

