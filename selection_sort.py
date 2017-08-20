# Selection Sort 

arr = [31, 41, 59, 26, 41, 58]

def minValue(arr):
	minVal = arr[0]
	for i in range(1, len(arr)):
		if minVal > arr[i]:
			minVal = arr[i]
	return (minVal, arr.index(minVal))

def selectionSort(arr):
	sort_arr = []
	while len(arr) > 0:
		minVal, indexVal = minValue(arr)
		arr.pop(indexVal)
		sort_arr.append(minVal)
	print(sort_arr)

selectionSort(arr)