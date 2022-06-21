nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

class FlatIterator:
	def __init__(self, list_of_lists):
		self.list_of_lists = list_of_lists
		self.index = -1

	def __iter__(self):
		self.index += 1
		self.index_in_list = 0
		return self

	def __next__(self):
		if self.index_in_list == len(self.list_of_lists[self.index]):
			iter(self)
		if self.index == len(self.list_of_lists):
			raise StopIteration
		self.index_in_list += 1
		return self.list_of_lists[self.index][self.index_in_list - 1]


for item in FlatIterator(nested_list):
	print(item) 

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)