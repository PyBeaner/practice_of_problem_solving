class Stack:
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items == []
	
	def size(self):
		return len(self.items)
		
	def peek(self):
		return self.items[-1]
		
	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		return self.items.pop()
		
