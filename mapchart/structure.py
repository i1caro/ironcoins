class Fringe(object):
	inside = list()
	index = dict()
	size = 0
	
	def update(self, where, item):
		index_number = self.index.get(item, None)
		if index_number:
			self.inside.pop(index_number)
		else:
			self.size+=1
		self.inside.insert(where, item)
		self.index[item] = where

	def pop(self, where):
		node = self.inside.pop(where)
		self.index.pop(node)
		self.size-=1

	def __getitem__(self, where):
		return self.inside[where]

	def __len__(self):
		return self.size




