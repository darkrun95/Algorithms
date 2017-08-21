# Maximum subarray in linear time

from math import inf
arr = [-8, 2, 3, 1, -1, -7, 10, -10]

def maximum_subarray(arr):
	max_sum = 0
	current_sum = 0

	for i in range(0, arr.__len__()):
		current_sum = current_sum + arr[i]
		if current_sum < 0:
			current_sum = 0

		if max_sum < current_sum:
			max_sum = current_sum

	return max_sum

max_sum = maximum_subarray(arr)
print(max_sum)