# Check if str2 is a rotation of str1
def IsRotation(str1, str2):
	if len(str1) == len(str2):
		return True if str2 in str1+str1 else False
	return False