# sorting then seeing if they're the same, shorter and cleaner, though not necessarily optimal
def checkPermutations_1(str1, str2):
	if len(str1) != len(str2):
		return False
	return ''.join(sorted(str1)) == ''.join(sorted(str2))


# compare character counts of the two strings
from collections import defaultdict

def checkPermutations_2(str1, str2):
	if len(str1) != len(str2):
		return False
	charDict = defaultdict(int)
	for c in str1:
		charDict[c] += 1
	for c in str2:
		charDict[c] -= 1
		if charDict[c] < 0:
			return False
	return True

