# Binary Insertion Sort [time complexity : O(nlogn)]

arr = [31, 41, 59, 26, 41, 58]

# Binary Search module used for insertion
def binary_insert(arr, low, high, key):
	if low <= high:
		mid = (low + high)//2
		if key > arr[mid]:
			low = mid + 1
			binary_insert(arr, low, high, key)
		elif key <= arr[mid]:
			high = mid - 1
			binary_insert(arr, low, high, key)
	else:
		arr.insert(low, key)
	return

def binary_insertion_sort(arr):
	arr_length = arr.__len__()
	for j in range(1, arr_length):
		key = arr.pop(j)
		i = j - 1
		
		binary_insert(arr, 0, i, key)
	print(arr)

binary_insertion_sort(arr)