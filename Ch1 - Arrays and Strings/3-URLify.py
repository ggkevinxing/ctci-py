def URLify(s, trueLen):
	# move through string s in reverse, replace spaces and move characters
	# given that our string has an extra buffer, we need not worry about overwriting anything
	ind = len(s)
	sList = list(s)
	for i in reversed(range(trueLen)):
		if sList[i] == ' ':
			sList[ind-3:ind] = '%20'
			ind -= 3
		else:
			sList[ind-1] = sList[i]
			ind -= 1
	return ''.join(sList)