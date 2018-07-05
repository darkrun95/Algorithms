sample_string = "My name is Arun Pottekat"
find_string = "Arun"

from karp_rabin import KarpRabin
obj = KarpRabin()
obj.string_search(sample_string, find_string)
print(obj.time_taken)