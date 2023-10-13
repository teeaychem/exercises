# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# So, it's steps[n-1] + steps[n-2]
# As, if you've figured out all the ways of getting one or two steps distance, there's only two options.
# This is an offset fib, so there's no simple direct solution.


def climbStairs(n: int) -> int:
	record = [0] * max(n + 1, 2)
	record[1] = 1
	record[2] = 2
	for i in range(3,n + 1):
		record[i] = record[i-1] + record[i-2]
	return record[n]

print(climbStairs(n=3))