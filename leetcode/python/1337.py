# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

# A row i is weaker than a row j if one of the following is true:

# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

def kWeakestRows(mat: [[int]], k: int):
	
	sA = [] # summed array
	
	# sum the rows
	for i in range(0, len(mat)):
		s = 0
		for j in range(0, len(mat[i])):
			s += mat[i][j]
		sA.append(s)

	wR = []

	# go through the summed array
	# insert index as soon as exceeds 
	# indexes already added

	# alternative is to stable sort and return indicies

	for i in range(0, len(sA)):
		for j in range(0,i):
			if sA[wR[j]] <= sA[i]: # note, j index of sA from sorted indicies
				j += 1
			else:
				break # break as soon as inequality fails
		wR = wR[:j] + [i] + wR[j:]
	
	return wR[:k]

print(kWeakestRows(mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]], k = 3))
print(kWeakestRows(mat = [[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]], k = 2))

