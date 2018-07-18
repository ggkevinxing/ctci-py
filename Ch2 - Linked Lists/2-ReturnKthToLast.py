class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

# we can have two pointers, and send a pointer k steps forward and then advance both pointers so that
# the one not advanced initially will end up in the kth to last position when the other pointer reaches the end
def ReturnKthToLast(head):
	kth = head
	end = head
	for i in range(0, k):
		if end == None:
			return None
		end = end.next
	while end != None:
		kth = kth.next
		end = end.next
	# return kth.val
	return kth