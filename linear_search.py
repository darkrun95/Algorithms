# Linear Search

# Predefined list of numbers
arr = [31, 41, 59, 26, 41, 58]

# Linear Search Module
def linear_search(arr, key):
	for value in arr:
		if key == value:
			return (True, arr.index(value))
	return (False, -1)

# Accept Search Key from user and type cast into integer
searchKey = int(input("Enter Key:- "))

returnVal = linear_search(arr, searchKey)
if returnVal[0]:
	print("True:",returnVal[1])
else:
	print("False:",returnVal[1])