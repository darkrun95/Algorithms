# Insertion Sort 

arr = []
for i in range(0,10):
	arr.append(10 - i)

def insertionSort(arr):
	for j in range(1, arr.__len__()):
		key = arr[j]
		i = j - 1
		while arr[i] > key and i >= 0:
			arr[i+1] = arr[i]
			i = i - 1

		arr[i+1] = key
	print(arr)

insertionSort(arr)