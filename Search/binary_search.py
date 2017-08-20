# Binary Search

# Pre-requisite - Sorted Sequence of numbers
arr = [26, 31, 41, 41, 58, 59]

def binary_search(arr, low, high, searchKey):
	mid = (high + low)//2
	
	# Check condition to prevent infinite recursion
	if low <= high:
		if arr[mid] == searchKey:
			print("True:", mid)
			return 
		elif arr[mid] < searchKey:
			low = mid + 1
			binary_search(arr, low, high, searchKey)
		elif arr[mid] > searchKey:
			high = mid - 1
			binary_search(arr, low, high, searchKey)
	else:
		print("False: -1")
		return

searchKey = int(input("Enter Key:- "))

# Initialization indices
low = 0
high = arr.__len__() - 1

binary_search(arr, low, high, searchKey)