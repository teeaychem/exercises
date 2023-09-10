# Given n orders, each order consist in pickup and delivery services. 

# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

# Since the answer may be too large, return it modulo 10^9 + 7.

 

# Example 1:

# Input: n = 1
# Output: 1
# Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
# Example 2:

# Input: n = 2
# Output: 6
# Explanation: All possible orders: 
# (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
# This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
# Example 3:

# Input: n = 3
# Output: 90

def sum(n):
	total = 0
	for i in range(1,n+1):
		total += i
	return total

class Solution:
	def countOrders(n: int):
		history = [0,1]
		for i in range(2,n+1):
			# history.append(sum((2 * (i - 1)) + 1) * history[i-1])
			x = (2 * (i - 1)) + 1
			history.append((x * (x + 1) // 2) * history[i-1])
		return history[n] % ((10 ** 9) + 7)

print(sum(2))
print(Solution.countOrders(n=2))

# This turned out to be a thinking thing.
# Observation is that from the solution to n-1 we can work out the solution to n but considering where the pickup and delivery can be distributed.
# For, given the solution to n-1 there are (solution(n-1) + 1) different pickup/delivery points.
# So, then, there are this many options if pickup happens first.
# One fewer if pickup happens second, and so on.

# Though, apparently this is very slow.

# Okay, Euler for sum helps.

