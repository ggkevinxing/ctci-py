class Graph:
	def __init__(self, nodes):
		self.nodes = nodes

class Node:
	def __init__(self, name, val):
		self.name = name
		self.val = val
		self.children = []
		self.visited = False

def IsRouteBetween_BFS(graph, start, end):
	for node in graph.nodes:
		node.visited = False
	if node1 == node2:
		return True

	q = [start]
	# alternately, instead of having a visited field
	# we can have a hash set to represent our visited nodes
	# seen = set()
	while q != []:
		currNode = q.pop(0)
		for node in currNode.children:
			if node.visited == False:
				if node == end:
					return True
				else:
					q.append(node)
		currNode.visited = True

def IsRouteBetween_DFS(graph, start, end):
	return IsRouteBetween_DFS_Recursive(start, end)

def IsRouteBetween_DFS_Recursive(start, end):
	if start == end:
		return True
	if start.children == []:
		return False
	else:
		res = False
		for node in start.children:
			return res or IsRouteBetween_DFS_Recursive(node, end)