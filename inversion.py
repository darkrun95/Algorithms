# Inversion Algorithm - based on insertion sort [ Time complexity - O(n*n) ]

a = [2, 3, 8, 6, 1]

# Inversion module
def inversion(a):
	count = 0
	for i in range(0, a.__len__()-1):
		for j in range(i+1, a.__len__()):
			if a[i] > a[j]:
				count = count + 1
	return count

val = inversion(a)
print(val)