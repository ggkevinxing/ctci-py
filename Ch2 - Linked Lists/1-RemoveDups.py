class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
# Remove duplicates in an unsorted linked list
# FOLLOW UP what if we weren't allowed to use extra buffers?
def RemoveDups(node):
	seen = set()
	prevNode = None
	currNode = node
	while currNode != None:
		nVal = currNode.val
		if nVal in seen:
			prevNode.next = currNode.next
		else:
			seen.add(nVal)
			prevNode = currNode
		currNode = currNode.next

# Still two pointers, but instead of one pointing to previous node, we have a runner pointer go through each node to
# check if they're the same as the current node's value, and if they are remove them
# This removes duplicates in place without extra space complexity with a hash set buffer, but takes n^2 time instead of n time with n space
def RemoveDups_FollowUp(node):
	currNode = node
	while currNode != None:
		runnerNode = currNode
		while runnerNode.next != None:
			if currNode.val == runnerNode.next.val:
				runnerNode.next = runnerNode.next.next
			else:
				runnerNode = runnerNode.next
		currNode = currNode.next