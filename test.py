from random import sample
from random import seed

seed(0)
arr = sample(range(1,100000),10000)

arr_copy = arr.copy()
from insertion import Insertion
obj = Insertion(arr_copy)
obj.sort()
print("Insertion: \t{}s".format(obj.time_taken))

arr_copy = arr.copy()
from merge import MergeSort
obj = MergeSort(arr_copy)
obj.sort()
print("Merge Sort: \t{}s".format(obj.time_taken))

arr_copy = arr.copy()
from heap import HeapSort
obj = HeapSort(arr_copy)
obj.sort()
print("Heap Sort: \t{}s".format(obj.time_taken))

arr_copy = arr.copy()
from bst import Bst
obj = Bst(arr_copy)
obj.sort()
print("BST Sort: \t{}s".format(obj.time_taken))

arr_copy = arr.copy()
from avl import AVL
obj = AVL(arr_copy)
obj.sort()
print("AVL Sort: \t{}s".format(obj.time_taken))

arr_copy = arr.copy()
from radix import Radix
obj = Radix(arr_copy)
obj.sort()
print("Radix Sort: \t{}s".format(obj.time_taken))