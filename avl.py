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
		self.height_diff = 0
		self.height = 0

class AVL():
	"""
	AVL Sort:
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
		self.arr = arr.copy()
		self.sorted_arr = []
		self.unsorted_arr = arr.copy()
		self.begin_node = TreeNode(self.arr.pop(0))

	def left_rotate(self, node):
		"""
		Left rotate to maintain balance factor

		Parameters:
		node: Node around which the tree has to be left rotated
		"""
		right_tree = node.rchild
		left_tree = node
		left_tree.rchild = None
		right_tree.parent = None

		left_tree.rchild = right_tree.lchild
		if right_tree.lchild:
			right_tree.lchild.parent = left_tree
		right_tree.lchild = None

		side = ""
		if left_tree.parent:
			if left_tree.parent.lchild == left_tree:
				side = "LEFT"
			else:
				side = "RIGHT"	

		right_tree.parent = left_tree.parent
		left_tree.parent = right_tree
		right_tree.lchild = left_tree

		if side == "LEFT":
			right_tree.parent.lchild = right_tree
		elif side == "RIGHT":
			right_tree.parent.rchild = right_tree
		else:
			self.begin_node = right_tree

		self.update_height(left_tree)
		return

	def right_rotate(self, node):
		"""
		Right rotate to maintain balance factor

		Parameters:
		node: Node around which the tree has to be right rotated
		"""
		left_tree = node.lchild
		right_tree = node
		right_tree.lchild = None
		left_tree.parent = None

		right_tree.lchild = left_tree.rchild
		if left_tree.rchild:
			left_tree.rchild.parent = right_tree
		left_tree.rchild = None

		side = ""
		if right_tree.parent:
			if right_tree.parent.lchild == right_tree:
				side = "LEFT"
			else:
				side = "RIGHT"	

		left_tree.parent = right_tree.parent
		right_tree.parent = left_tree
		left_tree.rchild = right_tree

		if side == "LEFT":
			left_tree.parent.lchild = left_tree
		elif side == "RIGHT":
			left_tree.parent.rchild = left_tree
		else:
			self.begin_node = left_tree

		self.update_height(right_tree)
		return

	def update_height(self, node):
		"""
		Iteratively update height and the balance factor for the 
		given node and nodes above

		Parameters:
		node: Node to update height and balance factor
		"""
		while node:
			lchild_height, rchild_height = -1, -1
			if node.lchild:
				lchild_height = node.lchild.height

			if node.rchild:
				rchild_height = node.rchild.height

			node.height = max(lchild_height, rchild_height) + 1
			node.height_diff = rchild_height - lchild_height
			node = node.parent
		return
	
	def check_avl(self, node):
		"""
		Check whether the given node satisfies the AVL property

		Parameters:
		node: node to be checked for AVL property
		"""
		if node:
			if node.height_diff < -1:
				if node.lchild.height_diff < 0:
					self.right_rotate(node)
				else:
					self.left_rotate(node.lchild)
					self.right_rotate(node)
					return
			elif node.height_diff > 1:
				if node.rchild.height_diff > 0:
					self.left_rotate(node)
				else:
					self.right_rotate(node.rchild)
					self.left_rotate(node)
			self.check_avl(node.parent)
		return

	def build_avl(self):
		"""
		Build AVL Tree from unordered array
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

			self.update_height(current_node)
			self.check_avl(current_node)
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
		Initiate the avl sort module
		"""
		start_time = self.time.time()
		self.build_avl()
		self.inorder_tracing(self.begin_node)
		end_time = self.time.time()
		self.time_taken = round(end_time - start_time, 3)
		return