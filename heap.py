class HeapSort():
	"""
	Heap Sort:
	Parameters: 
	arr: Unsorted array

	Attributes:
	sorted_arr: Sorted array
	unsorted_arr: copy of unsorted array
	time_taken: time taken by module to finish sorting

	Modules imported:
	time: to calculate running time for the sorting module	
	math: ceil() - To calculate upper bound limit of array
	"""

	def calculate_upper_limit(self):
		self.upper_limit = self.math.ceil((len(self.arr)-1)/2) - 1
		return
	
	def max_heapify(self, arr_index):
		"""
		Shift position of array element to maintain max heap property

		Parameters: 
		arr_index: Index of array element to be checked for max heap property
		"""
		lchild_index = (2 * arr_index) + 1
		if (lchild_index // 2) > self.upper_limit:
			return
		else:
			if 2 * (arr_index + 1) == len(self.arr):
				if self.arr[arr_index] < self.arr[lchild_index]:
					self.arr[lchild_index], self.arr[arr_index] = self.arr[arr_index], self.arr[lchild_index]
					self.max_heapify(lchild_index)	
			else:
				rchild_index = 2 * (arr_index + 1)
				lchild_flag, rchild_flag = False, False
				if self.arr[arr_index] < self.arr[lchild_index]:
					lchild_flag = True

				if self.arr[arr_index] < self.arr[rchild_index]:
					rchild_flag = True

				if lchild_flag and rchild_flag:
					if self.arr[lchild_index] < self.arr[rchild_index]:
						self.arr[rchild_index], self.arr[arr_index] = self.arr[arr_index], self.arr[rchild_index]
						self.max_heapify(rchild_index)
					else:
						self.arr[lchild_index], self.arr[arr_index] = self.arr[arr_index], self.arr[lchild_index]
						self.max_heapify(lchild_index)
				elif lchild_flag:
					self.arr[lchild_index], self.arr[arr_index] = self.arr[arr_index], self.arr[lchild_index]
					self.max_heapify(lchild_index)	
				elif rchild_flag:
					self.arr[rchild_index], self.arr[arr_index] = self.arr[arr_index], self.arr[rchild_index]
					self.max_heapify(rchild_index)
		return		

	def build_maxheap(self):
		"""
		Build max-heap tree from the given unordered array
		"""
		for i in range(self.upper_limit, -1, -1):
			self.max_heapify(i)
		return 

	def __init__(self, arr):
		self.time = __import__('time')
		self.math = __import__('math')
		self.time_taken = None
		self.arr = arr.copy()
		self.sorted_arr = []
		self.unsorted_arr = arr.copy()
		self.upper_limit = 0
		
		self.calculate_upper_limit()
		self.build_maxheap()

	def sort(self):
		"""
		Initiate the heap sort module

		Returns:
		self: Object
		"""
		start_time = self.time.time()
		while len(self.arr) > 1:
			self.arr[0], self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1], self.arr[0]
			self.sorted_arr.append(self.arr[len(self.arr)-1])
			self.arr.pop()
			self.calculate_upper_limit()
			self.max_heapify(0)
		self.sorted_arr.append(self.arr[0])
		end_time = self.time.time()					
		self.time_taken = end_time - start_time
		return 