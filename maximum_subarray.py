# Maximum Sub-Array

from math import inf
arr = [-8, 2, 3, 1, -1, -3, 5, -10]

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
	for i in range(mid+1, high):
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

low_index, high_index, max_sum = max_subarray(arr, 0, arr.__len__() - 1)
print(low_index, high_index, max_sum)