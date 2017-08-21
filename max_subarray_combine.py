from math import inf
from time import time
from random import sample, seed

# Method to find max crossing subarray
def max_crossing_subarray(arr, low, mid, high):
	left_sum, right_sum = -inf, -inf

	sum_val = 0
	max_left = mid
	for i in range(mid, low-1, -1):
		sum_val = sum_val + arr[i]
		if sum_val > left_sum:
			left_sum = sum_val
			max_left = i

	sum_val = 0
	max_right = mid+1
	for i in range(mid+1, high+1):
		sum_val = sum_val + arr[i]
		if sum_val > right_sum:
			right_sum = sum_val
			max_right = i

	return (max_left, max_right, left_sum + right_sum)

# Dividing method
def max_subarray(arr, low, high):
	if low == high:
		return (low, high, arr[low])
	else:
		mid = (low + high) // 2
		# Check left subarray
		left_low, left_high, left_sum = max_subarray(arr, low, mid)

		# Check right subarray
		right_low, right_high, right_sum = max_subarray(arr, mid+1, high)

		# Find cross subarray max sum and max index
		cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)

		if left_sum > right_sum and left_sum > cross_sum:
			return (left_low, left_high, left_sum)
		elif right_sum > left_sum and right_sum > cross_sum:
			return (right_low, right_high, right_sum)
		else:
			return (cross_low, cross_high, cross_sum)

# Brute force method for finding maximum subarray
def maximum_subarray_brute_force(arr):
	max_sum = -inf
	left_index = 0
	right_index = 0
	for i in range(0, arr.__len__()):
		sum_val = 0
		# Check for contiguous array locations
		for j in range(i, arr.__len__()):
			sum_val = sum_val + arr[j]
			if sum_val > max_sum:
				max_sum = sum_val
				left_index = i
				right_index = j
	return (left_index, right_index, max_sum)

# Combined module using brute force and recursion
def max_subarray_combine(arr, low, high):
	if high - low <= 35:
		left_index, right_index, max_sum = maximum_subarray_brute_force(arr[low:high])
		return (left_index, right_index, max_sum)
	else:
		mid = (low + high) // 2
		left_low, left_high, left_sum = max_subarray(arr, low, mid)
		right_low, right_high, right_sum = max_subarray(arr, mid+1, high)
		cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)

		if left_sum > right_sum and left_sum > cross_sum:
			return (left_low, left_high, left_sum)
		elif right_sum > left_sum and right_sum > cross_sum:
			return (right_low, right_high, right_sum)
		else:
			return (cross_low, cross_high, cross_sum)

seed(10)
for i in range(1, 50):
	arr = sample(range(-25, 25), i)
	start_time = time()
	low_index, high_index, max_sum = max_subarray(arr, 0, arr.__len__() - 1)
	end_time = time()

	start_time_b = time()
	low_index_b, high_index_b, max_sum_b = maximum_subarray_brute_force(arr)
	end_time_b = time()

	start_time_c = time()
	low_index_c, high_index_c, max_sum_c = max_subarray_combine(arr, 0, arr.__len__() - 1)
	end_time_c = time()

	print(int((end_time - start_time) * 1000000), int((end_time_b - start_time_b) * 1000000), int((end_time_c - start_time_c) * 1000000))
