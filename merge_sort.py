# Merge Sort

arr = [31, 41, 59, 26, 41, 58]

# Conquer 
def merge(arr, low, mid, high):
	n1 = mid - low + 1
	n2 = high - mid

	L = []
	R = []
	for i in range(0,n1):
		L.append(arr[low + i])

	for i in range(0, n2):
		R.append(arr[mid + i + 1])

	i, j, k = 0, 0, low
	while i < n1 and j < n2:
		if L[i] < R[j]:
			arr[k] = L[i]
			i = i + 1
		else:
			arr[k] = R[j]
			j = j + 1
		k = k + 1

	while i < n1:
		arr[k] = L[i]
		i = i + 1
		k = k + 1

	while j < n2:
		arr[k] = R[j]
		j = j + 1
		k = k + 1

	return 

# Divide 
def merge_sort(arr, low, high):
	if low < high:
		mid = (low + high)//2
		merge_sort(arr, low, mid)
		merge_sort(arr, mid+1, high)
		merge(arr, low, mid, high)
	return

merge_sort(arr, 0, arr.__len__()-1)
print("Sorted Array: ", arr)