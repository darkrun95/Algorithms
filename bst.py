class TreeNode():
	"""
	Singular Tree node

	Parameters:
	data: Value contained by the node
	lchild: Pointer to the left child
	rchild: Pointer to the right child
	parent: Pointer to the parent node
	"""
	def __init__(self, data):
		self.data = data
		self.lchild = None
		self.rchild = None
		self.parent = None

class Bst():
	"""
	Bst Sort:
	Parameters: 
	arr: Unsorted array

	Attributes:
	sorted_arr: Sorted array
	unsorted_arr: copy of unsorted array
	time_taken: time taken by module to finish sorting

	Modules imported:
	time: to calculate running time for the sorting module	
	"""
	def __init__(self, arr):
		self.time = __import__('time')
		self.sorted_arr = []
		self.unsorted_arr = arr.copy()
		self.arr = arr.copy()
		self.time_taken = None
		self.begin_node = TreeNode(self.arr.pop(0))
		
	def build_tree(self):
		"""
		Build Binary Tree from unordered array
		"""
		while len(self.arr) > 0:
			current_node = self.begin_node
			new_node = TreeNode(self.arr.pop(0))

			while True:
				if current_node.data < new_node.data:
					if current_node.rchild:
						current_node = current_node.rchild
					else:
						current_node.rchild = new_node
						new_node.parent = current_node
						break
				else:
					if current_node.lchild:
						current_node = current_node.lchild
					else:
						current_node.lchild = new_node
						new_node.parent = current_node
						break
		return

	def inorder_tracing(self, node):
		"""
		Inorder traversal of tree to find sorted array

		Parameters:
		node: begin_node for the avl tree
		"""
		if node.lchild:
			self.inorder_tracing(node.lchild)

		self.sorted_arr.append(node.data)
		
		if node.rchild:
			self.inorder_tracing(node.rchild)
		return

	def sort(self):
		"""
		Initiate the bst sort module
		"""
		start_time = self.time.time()
		self.build_tree()
		self.inorder_tracing(self.begin_node)
		end_time = self.time.time()
		self.time_taken = round(end_time - start_time, 3)
		return