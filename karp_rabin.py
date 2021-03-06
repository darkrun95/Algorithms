class KarpRabin():
	"""
	Karp Rabin Algorithm: String matching algorithm in linear time.
	Parameters: 

	Attributes:
	time_taken: Time taken for completing sorting	
	
	Modules imported:
	time: to calculate running time for the sorting module	
	"""
	def __init__(self):
		self.time = __import__('time')
		self.time_taken = None

	def hash(self, hash_character):
		"""
		Division Hash function:
			h(x): k mod m

			k: Key to be hashed
			m: Prime number greater than the length of search string.
			   [ 13 selected for random reasons. ]

		Parameters:
		hash_character: Character for which hash value needs to be 
						calculated.
		"""
		hash_value = ord(hash_character) % 13
		return hash_value

	def sum_hash(self, hash_list):
		"""
		Return the sum of the hash function

		Parameters:
		hash_list: List of hash values that need to be summed.
		"""
		return sum(hash_list)

	def string_search(self, sample_string, find_string):
		"""
		String matching module

		Parameters:
		sample_string: Base string that needs to be searched.
		find_string: String that needs to be searched in the sample string.

		Additional Attributes:
		ht: List holding the hash values for the base string
		hs: List holding the hash values for the search string
		"""
		start_time = self.time.time()
		hs, ht = [], []

		# Hash values for search string
		for c in find_string:
			hs.append(self.hash(c))

		# Hash values for sample string for search string size
		for c in sample_string[: len(find_string)]:
			ht.append(self.hash(c))

		if self.sum_hash(hs) == self.sum_hash(ht):
			if find_string == sample_string[: len(find_string)]:
				print("Match found.")

		# Find hash value for base string and search string for per iteration of 
		# search string size
		for i in range(len(find_string), len(sample_string)):
			ht.pop(0)
			ht.append(self.hash(sample_string[i]))

			if self.sum_hash(hs) == self.sum_hash(ht):
				if find_string == sample_string[i-len(find_string)+1: i+1]:
					print("Match found")
					end_time = self.time.time()					
					self.time_taken = round(end_time - start_time, 3)
					return 

		print("Match not found")
		end_time = self.time.time()					
		self.time_taken = round(end_time - start_time, 3)
		return
