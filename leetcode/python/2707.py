# You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

# Return the minimum number of extra characters left over if you break up s optimally.

 

# Example 1:

# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

# Example 2:

# Input: s = "sayhelloworld", dictionary = ["hello","world"]
# Output: 3
# Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
 
# Constraints:

# 1 <= s.length <= 50
# 1 <= dictionary.length <= 50
# 1 <= dictionary[i].length <= 50
# dictionary[i] and s consists of only lowercase English letters
# dictionary contains distinct words

# non-overlapping substrings means, I think, that no element of the string appears in two substrings.

# Initial recursive version:

def remove(string, entry):
	return string.replace(entry, "")

def minExtraCharHelper(string, list):
	if not list:
		return len(string)
	elif len(list) == 1:
		return minExtraCharHelper(remove(string, list[0]), list[1:])
	else:
	 	return min(  
	 		minExtraCharHelper(remove(string, list[0]), list[1:]),
	 		minExtraCharHelper(string, list[1:])
	 	)

def minExtraChar(string, list):
	return minExtraCharHelper(string, list)

# Version with memoing.
# Note, only check the end of the string, as any other replacement will have been made earlier.
# Careful to ensure range is large enough.

def again(string, dictionary):

	substringLowest = [float('inf')] * (len(string) + 1)
	substringLowest[0] = 0

	for i in range(1, len(string) + 1):
		for entry in dictionary:
			if i >= len(entry) and entry == string[i - len(entry):i]:
					substringLowest[i] = min(substringLowest[i], substringLowest[i - len(entry)])
		substringLowest[i] = min(substringLowest[i], (substringLowest[i - 1]) + 1)
	
	return substringLowest[len(string)]


print(minExtraChar("dwmodizxvvbosxxw", 
									 ['txhe', 'cehy', 'tskz', 'kzbu', 'diz', 'ksv', 'nuq', 'wmo', 'ox', 'lb', 'gu', 'ds', 'v', 'o', 'r', 'e'])) # 7

print(minExtraChar("azvzulhlwxwobowijiyebeaskecvtjqwkmaqnvnaomaqnvf",
									["na","i","edd","wobow","kecv","b","n","or","jj","zul","vk","yeb","qnfac","azv","grtjba","yswmjn","xowio","u","xi","pcmatm","maqnv"]))  # 15

# memoing makes a huge difference here!

print(minExtraChar("hmiywboxlwnoummzgnptpyemzmpdech",
									["iy","voiu","pd","w","gpxxn","ckao","zkxod","udylc","g","a","vkv","egrg","qolqi","r","x","inucv","c","noum","stiut","vyukt","lyql","pzxlr","zjw","dw","e","box","y","kb","tpye","bma","ndadr","z","oqf","cyu","wh","joka","mtm","wpy","km","mzg","grps","me"])) # 8

