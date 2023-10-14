# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# Conceptually simple, but need to be careful on the details.
# low needs to be either inf or the first price, as there's no way to tell in advance what the lowest may be.
# high needs to be reset every time low is set. 
# It's always fine to buy low and reset high as this guarantees an greater diff than previous low, if a diff exists.
# Need to check whether diff is worth updating.

# On second look, the first check isn't needed as there's always at least one price.
# And, the last max check isn't needed as the diff must always be positive.

def maxProfit(prices: List[int]) -> int:
	if len(prices) < 1: # stop if no prices
		return 0

	low = prices[0]
	high = 0
	diff = 0
	for i in prices:
		if i < low: # buy
			low = i
			high = 0 # reset highest sale point
		elif i > high: # only consider if no buy
			high = i
			if (high - low) > diff: # only update diff if better
				diff = (high - low)
	return max(diff,0)

# Given the two redundant checks, this apparently beat 91% on speed and 94% n memory, which I think illustrates these stats aren't worth much.