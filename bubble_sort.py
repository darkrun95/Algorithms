# Bubble Sort 

arr = [31, 41, 59, 26, 41, 58]

def bubbleSort(arr):
	for i in range(0, arr.__len__() - 2):
		for j in range(arr.__len__() - 1, i, -1):
			if arr[j] < arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
	return 

bubbleSort(arr)
print(arr)