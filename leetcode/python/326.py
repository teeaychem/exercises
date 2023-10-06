# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).

# Very simple is to continuously divide:

def isPowerOfThree(n: int) -> bool:
	m = 1
	while m < n:
		m *= 3
	return n == m


print(isPowerOfThree((3**8)))
print(isPowerOfThree((3**8) - 1))

# Though, it's a little more efficient to attempt to recreate by multiplying

def isPowerOfThreeUp(n: int) -> bool:

	return n % 3

print(isPowerOfThreeUp((3**8)))
print(isPowerOfThreeUp((3**8) - 1))


