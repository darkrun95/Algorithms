# Horner's Rule for evaluating polynomial expressions.

# coefficiens for a i.e. a1, a2, a3
a = [1, 2, 3]
n = 3

# Value for x
x = 2

def horners_method(a, n, x):
	y = 0 
	for k in range(n-1,-1,-1):
		y = a[k] + (x*y)
	return y

val = horners_method(a, n, x)
print(val)