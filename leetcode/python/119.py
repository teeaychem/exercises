# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]

# Generate each row.
# If 1 indexed length of row is equal to row number.
# So, create initial row with 1s.
# Start and end are 1, so only need to fill middle.
# Do this by looking at the previous row.

def getRow(rowIndex: int) -> [int]:
	rows = []
	for i in range(0,rowIndex + 3):
		row = [1] * i
		for j in range(1,i - 1):
			row[j] = rows[i-1][j-1] + rows[i-1][j]
		rows.append(row)
	return rows[rowIndex + 1]

print(getRow(rowIndex=0))
print(getRow(rowIndex=3))
print(getRow(rowIndex=1))

# This 'beat' 96% for memory.
# But, this uses a lot of unnecessary memory when the rows get big.
# For, there's no need to store all the previous rows.
# More efficient:

def getRow2(rowIndex: int) -> [int]:
	prevrow = []
	for i in range(0,rowIndex + 2):
		row = [1] * i
		for j in range(1,i - 1):
			row[j] = prevrow[j-1] + prevrow[j]
		prevrow = row
	return row

print(getRow2(rowIndex=0))
print(getRow2(rowIndex=3))
print(getRow2(rowIndex=1))

# This beat 20%.
# lol