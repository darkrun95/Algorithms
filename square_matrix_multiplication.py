# Square Matrix Multiplication - Time complexity [O(n*n*n)]

import numpy as np

# Random 2D array using numpy
A = np.random.rand(2,2)
B = np.random.rand(2,2)

# matrix multiplication module

def matrix_multiplication(A, B):
	C = []
	rows = A.__len__() 
	for i in range(0, rows):
		c_row = []
		for j in range(0, rows):
			c_sum = 0
			for k in range(0, rows):
				c_sum = c_sum + A[i][k] * B[k][j]
			c_row.append(c_sum)
		C.append(c_row)

	return C

C = matrix_multiplication(A, B)

# Check answer using numpy's dot method
print(C)
print(np.dot(A, B))