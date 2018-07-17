# Check if string str1 is one (or zero) edits away from other string str2
def IsOneAway(str1, str2):
	if str1 == str2:
		return True
	if len(str1) == len(str2):
		diffChars = 0
		for i in range(0, len(str1)):
			if str1[i] != str2[i]:
				diffChars += 1
				if diffChars > 1:
					return False
	if abs(len(str1) - len(str2)) > 1:
		return False
	else:
		if len(str1) > len(str2):
			return CheckOneInsert(str1, str2)
		else:
			return CheckOneInsert(str2, str1)

def CheckOneInsert(str1, str2):
	print(str1)
	print(str2)
	i = 0
	j = 0
	diffChars = 0
	while i < len(str1) and j < len(str2):
		if str1[i] != str2[j]:
			diffChars += 1
			if diffChars > 1:
				return False
			i += 1
		else:
			i += 1
			j += 1
	return True