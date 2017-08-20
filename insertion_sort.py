# Insertion Sort 

arr = [31, 41, 59, 26, 41, 58]

def insertionSort(arr):
	for j in range(1, arr.__len__()):
		key = arr[j]
		i = j - 1
		print("while loop")
		while arr[i] > key and i >= 0:
			arr[i+1] = arr[i]
			i = i - 1
			print(arr)

		arr[i+1] = key
		print("\nfor loop")
		print(arr)
		print()

	print("\nEnd Insertion sort")
	print(arr)

insertionSort(arr)