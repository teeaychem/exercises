# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

# A naive solution.
# Instead of (i * 1)^2 could do i^2 and return (i - 1).

def mySqrt(x: int) -> int:
	i = 0
	while (i + 1) * (i + 1) <= x:
		i += 1
	return i

print(mySqrt(4))
print(mySqrt(8))

