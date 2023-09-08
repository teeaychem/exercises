# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]


class Solution:
	def generate(numRows: int):
		triangle = [[1]]
		for i in range(1,numRows):
			newRow = [1]
			for j in range(0,len(triangle[i-1]) - 1):
				newRow.append(triangle[i-1][j] + triangle[i-1][j+1])
			newRow.append(1)
			triangle.append(newRow)
		
		return triangle #[:numRows]
		
print(Solution.generate(numRows=1))
print(Solution.generate(numRows=2))		
print(Solution.generate(numRows=3))
print(Solution.generate(numRows=4))

# This is not particularly elegant.
# Still, it works fine.

# Wrt previous commit, this runs with most memory and slowest time, so the comparisons should be ignored.