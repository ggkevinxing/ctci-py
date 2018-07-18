class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

# Middle node meaning any node that isn't the beginning of end of the linked list, just an in-between node
# While we can't reassign the next value of the previous node's next node to effectively delete the given node,
# we can take the given node's next node's value and replace our given node's value. We can then take our next
# node's next node and then we'll delete them, effectively taking their place

# Assumptions: We are not given the head or end node as input
def DeleteMiddleNode(node)
	if node == None or node.next == None:
		return	# given an invalid node as input, just stop
	nextNode = node.next # we will steal its val and next
	node.val = nextNode.val
	node.next = nextNode.next