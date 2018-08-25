# coding: utf-8
class heap:
	def __init__(self, dir=-1):
		'''one indexed heap'''
		self.items = [None]
		self.size = 0
		self.dir = dir
		
	def parentIndex(self, i):
		if i <= 1:
			return None
		return i//2
		
	def leftChildIndex(self, i):
		l = i*2
		if l > self.size:
			return None
		else:
			return l
			
	def rightChildIndex(self, i):
		r = i*2 + 1
		if r > self.size:
			return None
		else:
			return r
	
	def parent(self, i):
		p = self.parentIndex(i)
		if p==None:
			return None
		else:
			return self.items[p]
			
	def leftChild(self, i):
		l = self.leftChildIndex(i)
		if l == None:
			return None
		else:
			return self.items[l]
	
	def rightChild(self, i):
		r = self.rightChildIndex(i)
		if r==None:
			return None
		else:
			return self.items[r]
	
	def add(self, item):
		self.items.append(item)
		self.size += 1
		self.heapifyUp()
		
	def pop(self):
		if self.size < 1:
			return None
		popped = self.items[1]
		self.items[1] = self.items[self.size]
		self.items.pop(-1)
		self.size -= 1
		self.heapifyDown()
		return popped
		
	def peek(self, i=1):
		if i > 0 and i <= self.size:
			return self.items[i]
		return None
		
	def swap(self, ai, bi):
		temp = self.items[ai]
		self.items[ai] = self.items[bi]
		self.items[bi] = temp
		
	def heapifyUp(self):
		'''
		p > i, * -1, < 0
		p < i, * -1, > 0
		p > i, *  1, > 0
		p < i, *  1, < 0
		'''
		#print('heapifyup')
		if self.size == 1:
			return 
		i = self.size
		while True:
			#print('p', self.parent(i), 'i', self.items[i], self.dir)
			
			if self.parentIndex(i) != None and (self.parent(i) - self.items[i]) * self.dir < 0:
				#print(self.parentIndex(i), (self.parent(i) - self.items[i]) * self.dir)
				#print('swapping')
				self.swap(i, self.parentIndex(i))
				i = self.parentIndex(i)
			else:
				break
			
	def heapifyDown(self):
		if self.size == 1:
			return 
		i = 1
		while self.leftChildIndex(i) != None:
			indexToSwap = self.leftChildIndex(i)
			if self.rightChildIndex(i) != None and (self.rightChild(i) - self.leftChild(i)) * self.dir > 0:
				indexToSwap = self.rightChildIndex(i)
				
			if (self.items[i] - self.items[indexToSwap]) * self.dir < 0:
				self.swap(i, indexToSwap)
				i = indexToSwap
				
			else:
				break
