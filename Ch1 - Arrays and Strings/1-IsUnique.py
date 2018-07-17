# Assumptions: For simplicity, our given string will be an ASCII string

def IsUnique(inputStr):
	if len(inputStr) > 128:
		return False
	seen = set()
	for c in inputStr:
		if c in seen:
			return False
		seen.add(c)
	return True