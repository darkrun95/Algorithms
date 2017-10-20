class Insertion():
	"""
	Insertion Sort

	Parameters:
	arr: Unordered array to be sorted

	Attributes: 
	unsorted_arr: copy of unsorted array
	sorted_arr: Sorted array
	time_taken: Time taken for completing sorting	
	"""

	def __init__(self, arr):
		"""
		Import statements:
		time: Measuring time needed for completion
		"""

		self.time = __import__('time')

		self.unsorted_arr = arr.copy()
		self.sorted_arr = arr.copy()
		self.time_taken = None

	def sort(self):
		"""	
		Sorting unsorted array using insertion sort 
		
		Returns:
		self: Insertion Object containing sorted array
		"""
		start_time = self.time.time()
		for i in range(1, len(self.sorted_arr)):
			key = i
			for j in range(i-1, -1, -1):
				if self.sorted_arr[key] < self.sorted_arr[j]:
					self.sorted_arr[key], self.sorted_arr[j] = self.sorted_arr[j], self.sorted_arr[key]
					key = key - 1
				else:
					break
		end_time = self.time.time()					
		self.time_taken = end_time - start_time
		return self