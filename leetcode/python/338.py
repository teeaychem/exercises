
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 
# Constraints: 
# # 0 <= n <= 105

# Unneeded, but nice func to get binary rep
def binary(n):
	i = n
	rep = []
	while i != 0:
		rep = [i % 2] + rep
		i = i // 2

	return rep

def binaryCount(n):
	i = n
	count = 0
	while i != 0:
		count += (i % 2)
		i = i // 2

	return count

def countBits(n):

	out = []

	for i in range(0,n + 1):
		out += [binaryCount(i)]
	
	return out

# test

print(countBits(2))
print(countBits(5))
print(countBits(6))
print(countBits(7))
print(countBits(8))
print(countBits(9))
print(countBits(10))
print(countBits(11))
print(countBits(12))
print(countBits(13))
print(countBits(14))
print(countBits(15))
print(countBits(16))

print(countBits(0))
print(countBits(2))
print(countBits(4))
print(countBits(8))
print(countBits(16))
print(countBits(32))



def getrep(n):

	def next(running):
		return running + list(map(lambda x : x + 1, running[1:-1])) + [1]

	def getSequence(pow):
		if pow == 0:
			seq = [0]
		else:
			seq = [0,1,1]
			while pow != 1:
				seq = next(seq)
				pow -= 1

		return seq 

	pow = 0
	while 2 ** pow <= n:
		pow += 1
	
	return getSequence(pow)[:n+1]

for i in range(0,9999):
	if countBits(i) != getrep(i):
		print(i)

