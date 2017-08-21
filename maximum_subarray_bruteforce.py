# Maximum Subarray problem using brute force [ Time complexity: O(n*n) ]

from math import inf
arr = [-8, 2, 3, 1, -1, -7, 5, -10]

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

print(left_index, right_index, max_sum)