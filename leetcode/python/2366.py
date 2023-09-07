class Solution:

	def minimumReplacement(nums: list[int]) -> int:

		nextUp = nums[-1]
		opCount = 0

		for i in range(1, len(nums) + 1):

			if nums[-i] > nextUp:

				thisOpCount = (nums[-i] // nextUp) - 1

				if (nums[-i] % nextUp) != 0:
					thisOpCount += 1
				
				opCount += thisOpCount
				
				nextUp = nums[-i] // (thisOpCount + 1)

			else:
				nextUp = nums[-i]
			
		return opCount

		# wtih fresh eyes, this worked out.
		# the idea is to divide by the current limit as much as possible until inside.
		# then, to figure out the new limit, just see what remains after subtracting the previous limit from the current value as many times as possible.
		# I think what I missed before was + 1 to the nextUp opCount div.
		# That, and getting distracted by remainder.	

print(Solution.minimumReplacement([8,2])) # 3
print(Solution.minimumReplacement([3,9,3])) # 2
print(Solution.minimumReplacement([3,9,3,9])) # 2
print(Solution.minimumReplacement([3,3,9])) # 0
print(Solution.minimumReplacement([5,1])) # 4
print(Solution.minimumReplacement([12,9,7,6,17,19,21]))
print(Solution.minimumReplacement([7,6,15,6,11,14,10])) # 10
print(Solution.minimumReplacement([1,13,15,2,5,14,12,17])) # 20
print(Solution.minimumReplacement([368,112,2,282,349,127,36,98,371,79,309,221,175,262,224,215,230,250,84,269,384,328,118,97,17,105,342,344,242,160,394,17,120,335,76,101,260,244,378,375,164,190,320,376,197,398,353,138,362,38,54,172,3,300,264,165,251,24,312,355,237,314,397,101,117,268,36,165,373,269,351,67,263,332,296,13,118,294,159,137,82,288,250,131,354,261,192,111,16,139,261,295,112,121,234,335,256,303,328,242,260,346,22,277,179,223])) # 17748

# print(Solution.minimumReplacement([7,6])) # 2
# print(7 // 6)
# print(14 // 3)
# print(8 % 4)

# def find(i,j):
# 	if i <= j:
# 		return [0, i]
# 	else:
# 		if i % j == 0:
# 			return [i // j, j]
# 		elif i % 2 == 0:
# 			v, x = find(i // 2, j)
# 			return [1 + (2 * v), x]
# 		else:
# 			v1, i1 = find(i // 2, j)
# 			v2, i2 = find(i // 2 + 1, j)
# 			return [1 + (v1 + v2), min(i1, i2)]

# print(find(9,3))
# print(find(8,2))

# def getGCD(i,j):
# 	if j == 0:
# 		return i
# 	else:
# 		return getGCD(j, i % j)

# def findX(i,j):
# 	if i % j == 0:
# 		return (i // j) - 1
# 	else:
# 		return 1 + (findX(i - getGCD(i,j), j))

# print(findX(5,2))

# def findX(i,j):
# 				if i > j:
# 					if i % j == 0:
# 						return [(i // j) - 1, j]
# 					else:
# 						a, b = findX(i - j, j)
# 						return [1	+ a, min(b, j)]
# 				else:
# 					return [0,min(i,j)]

# 			def find(i,j):
# 				if i < j or i == j:
# 					return [0, i]
# 				else:
# 					if i % j == 0:
# 						return [(i // j) - 1, j]
# 					elif i % 2 == 0:
# 						v, x = find(i // 2, j)
# 						return [1 + (2 * v), x]
# 					else:
# 						v1, i1 = find(i // 2, j)
# 						v2, i2 = find(i // 2 + 1, j)
# 						return [1 + (v1 + v2), min(i1, i2)]