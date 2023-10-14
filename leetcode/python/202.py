# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false

# Constraints:

# 1 <= n <= 231 - 1

def isHappy(n: int) -> bool:
		seen = set()
		while n not in seen:
				seen.add(n)
				s = str(n)
				n = 0
				for i in range(0, len(s)):
						n += int(s[i]) ** 2
				print(n)
				if n == 1:
						return True
				
		return False

print(isHappy(n=1))
print(isHappy(n=19))

# Looking at an alternative, I came across the Floyd Cycle detection algorithm.
# Create a test, and then run two instances.
# One instance runs the test once each step and the other twice each step
# As there's a fixed point or a loop fast will either get stuck in the fixed point and wait for slow to catch up.
# Or, fast will eventually catch slow on some step.

def squareSum(n: int) -> int:
	s = 0
	while n > 0:
		s += (n % 10) ** 2
		n = n // 10
	return s

def isHappy(n: int) -> bool:

		slow = squareSum(n=n)
		fast = squareSum(n=squareSum(n=n))

		while slow != fast:
			slow = squareSum(n=slow)
			fast = squareSum(n=squareSum(n=fast))
		
		return slow == 1
