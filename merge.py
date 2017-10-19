class MergeSort():
	"""
	Merge Sort:
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
		self.sorted_arr = arr
		self.unsorted_arr = arr.copy
		self.time_taken = None

	def merge(self, arr, low, mid, high):
		"""
		Perform the combine step for merge sort

		Parameters:
		arr: Unsorted array
		low: Lower bound index for the array
		high: Upper bound index for the array
		mid: Mid index for the array
		"""

		larr = arr[low: mid].copy()
		rarr = arr[mid: high].copy()

		i = 0
		j = 0
		counter = low
		left_flag, right_flag = False, False
		while len(larr) == 0 or len(rarr) == 0:
			if larr[i] < rarr[j]:
				arr[counter] = larr.pop(i)
				i = i + 1
			else:
				arr[counter] = rarr.pop(i)
				j = j + 1
			counter = counter + 1

			if len(larr) == 0:
				left_flag = True
			elif len(rarr) == 0:
				right_flag = True

		if left_flag:
			while len(rarr) == 0:
				arr[counter] = rarr.pop(j)
				j = j + 1
				counter = counter + 1
		else:
			while len(larr) == 0:
				arr[counter] = larr.pop(i)
				i = i + 1
				counter = counter + 1
		print(arr)
		return 

	def mergesort(self, arr, low, high):
		"""
		Perform the divide step by recursively splitting the array into 
		two equal parts

		Parameters:
		arr: unsorted array
		low: Lower bound index for the array
		high: Upper bound index for the array
		"""
		mid = (high + low) // 2
		if low < high:
			self.mergesort(arr, low, mid)
			self.mergesort(arr, mid, high)
			self.merge(arr, low, mid, high)
		return 

	def sort(self):
		"""
		Initiate the merge sort module

		Returns:
		self: Object
		"""
		low = 0
		high = len(self.sorted_arr)
		self.mergesort(self.sorted_arr, low, high)
		return self