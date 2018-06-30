class Radix():
	"""
	Radix Sort:
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

		self.base = 10
		
	def counting_sort(self, counting_list):
		"""
		Module for performing counting sort

		Parameters:
		counting_list: The bits from the arr at the desired position for
					   performing counting sort.
		"""
		somelist = [[] for i in range(self.base)]
		for index, val in enumerate(counting_list):
			somelist[val].append(self.arr[index])

		self.sorted_arr.clear()
		for val in somelist:
			self.sorted_arr.extend(val)

		self.arr = self.sorted_arr
		return

	def sort(self):
		"""
		Initiate the radix sort module
		"""
		counter = 1
		start_time = self.time.time()
		while True:
			terminate = True
			counting_list = []
			for val in self.arr:
				digit = (val // counter) % 10
				if digit != 0:
					terminate = False
				counting_list.append(digit)

			counter = counter * 10
			self.counting_sort(counting_list)

			if terminate:
				break
				
		end_time = self.time.time()					
		self.time_taken = round(end_time - start_time, 3)
		return