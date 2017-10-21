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
		self.copy = __import__('copy')
		self.arr = arr.copy()
		self.sorted_arr = []
		self.unsorted_arr = arr.copy()
		self.begin_node = TreeNode(self.arr.pop(0))

	def left_rotate(self):
		return

	def right_rotate(self, node):
		node.lchild.parent = node.parent
		node.parent = node.lchild
		node.lchild = node.parent.rchild
		node.parent.rchild = node
		if not node.parent.parent:
			self.begin_node = node.parent
		return

	def check_avl(self, node):
		if node.parent:
			parent_node = node.parent
			if parent_node.height_diff < -1:
				if parent_node.lchild.height_diff < 0:
					self.right_rotate(parent_node)
				else:
					self.left_rotate()
					self.right_rotate()
			elif parent_node.height_diff > 1:
				if parent_node.rchild.height_diff > 0:
					self.left_rotate(parent_node)
				else:
					self.right_rotate()
					self.left_rotate()
			self.check_avl(parent_node)
		return

	def update_height(self, node):
		while node.parent:
			parent_node = node.parent
			lchild_height, rchild_height = -1, -1
			if parent_node.lchild:
				lchild_height = parent_node.lchild.height

			if parent_node.rchild:
				rchild_height = parent_node.rchild.height

			parent_node.height = max(lchild_height, rchild_height) + 1
			parent_node.height_diff = rchild_height - lchild_height
			node = parent_node
		return

	def build_avl(self):
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

			self.update_height(new_node)
			self.check_avl(new_node)
		return

	def inorder_tracing(self, node):
		if node.lchild:
			self.inorder_tracing(node.lchild)

		self.sorted_arr.append(node.data)
		
		if node.rchild:
			self.inorder_tracing(node.rchild)
		return

	def sort(self):
		start_time = self.time.time()
		self.build_avl()
		self.inorder_tracing(self.begin_node)
		end_time = self.time.time()
		self.time_taken = end_time - start_time
		return