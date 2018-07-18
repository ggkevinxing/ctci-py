class BSTNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

# In order to create a BST of minimum height given a list of numbers, we have to create a balanced BST;
# the left side and right side should roughly have the same number of nodes. Since our input array is
# already sorted, we can just pick the middle element to be the root of the tree
def ConstructMinimalBST(arrNums):
	return ConstructMinimalBST_Recursive(arrNums, 0, len(arrNums)-1)

def ConstructMinimalBST_Recursive(arrNums, start, end):
	if end < start:
		return None
	middleInd = (start + end) // 2
	ret = BSTNode(arrNums[middleInd])
	# print(ret.val)
	ret.left = ConstructMinimalBST_Recursive(arrNums, start, middleInd-1)
	ret.right = ConstructMinimalBST_Recursive(arrNums, middleInd+1, end)
	return ret