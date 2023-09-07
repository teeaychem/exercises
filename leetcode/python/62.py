# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

# grid = {}

# for i in range(0,10):
# 	grid[0,i] = 1
# for j in range(0,10):
# 	grid[j,0] = 1


# for i in range(1,10):
# 	for j in range(1,10):
# 		grid[i,j] = grid[i-1,j] + grid[i,j-1] # + grid[i-1,j-1]


def uniquePaths(n,m):
	grid = {}
	a = n - 1
	b = m - 1
	s = max(n,m)

	grid[0,0] = 1
	for i in range(0,s):
		grid[0,i] = 1
		grid[i,0] = 1
	for i in range(1,s):
		for j in range(1,s):
			grid[i,j] = grid[i-1,j] + grid[i,j-1] # + grid[i-1,j-1]

	return grid[a,b]

print(uniquePaths(1,1))
print(uniquePaths(2,2))
print(uniquePaths(2,3))
print(uniquePaths(2,6))
print(uniquePaths(3,7))
print(uniquePaths(2,1))


def uniquePathsRec(n,m):

	store = {}

	def uniquePathsRecHelper(n,m):
		if n == 0 or m == 0:
			return 1
		else:
			return uniquePathsRecHelper(n - 1,m) + uniquePathsRecHelper(n,m - 1)

	return uniquePathsRecHelper(n-1,m-1)

# print(uniquePathsRec(1,1))
# print(uniquePathsRec(2,2))
# print(uniquePathsRec(2,3))
# print(uniquePathsRec(2,6))
# print(uniquePathsRec(3,7))
# print(uniquePathsRec(2,1))

# Doing things with a grid is much faster than using a dictionary.

def uniquePathsB(n,m):
	
	grid = [[1] * m for i in range(0,n)]
	for i in range(1,n):
		for j in range(1,m):
			grid[i][j] = grid[i][j-1] + grid[i-1][j]

	return grid[n-1][m-1]

print(uniquePathsB(1,1))
print(uniquePathsB(2,2))
print(uniquePathsB(2,3))
print(uniquePathsB(2,6))
print(uniquePathsB(3,7))
print(uniquePathsB(2,1))

print(0 == "")