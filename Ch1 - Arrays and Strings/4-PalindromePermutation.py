# create a hash table of character counts, check to see if we have at most one odd character count
from collections import defaultdict
def IsPalindromePermutation(s):
	s = s.casefold()
	charDict = defaultdict(int)
	numOdds = 0
	for c in s:
		if c == ' ':
			continue
		charDict[c] += 1
	for k, v in charDict.items():
		if v % 2 == 1:
			numOdds += 1
			if numOdds > 1:
				return False
	return True
