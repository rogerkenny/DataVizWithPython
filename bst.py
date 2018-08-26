class bst():
	def __init__(self, val, parent=None, left=None, right=None, height=0):
		self.val = val
		self.parent = parent
		self.left = left
		self.right = right
		self.height = height

	def __repr__(self):
		# p = self.parent.val if self.parent != None else None
		# l = self.left.val if self.left != None else None
		# r = self.right.val if self.right != None else None
		# return "( V {} P {} L {} R {} )".format(self.val, p, l, r )
		return "({} h{})".format(self.val, self.height)


	def insert(self, n):
		if n.val <= self.val:
			if self.left == None:
				self.left = n
				n.parent = self
				self.height = 1
				return
			else:
				self.left.insert(n)
		if n.val > self.val:
			if self.right == None:
				self.right = n
				n.parent = self
				self.height = 1
				return
			else:
				self.right.insert(n)
		self.height = max((self.left.height if self.left != None else 0), (self.right.height if self.right != None else 0)) + 1

	def find(self, val):
		if self.val == val:
			return self
		if self.val > val:
			if self.left == None:
				return None
			else:
				return self.left.find(val)
		if self.val < val:
			if self.right == None:
				return None
			else:
				return self.right.find(val)

	def successor(self):
		if self.right != None:
			current = self.right
			while current.left != None:
				current = current.left
			return current

		current = self

		while current.parent != None:
			current = current.parent
			if current.val > self.val:
				return current
		
		return None

	def predecessor(self):
		if self.left != None:
			current = self.left
			while current.right != None:
				current = current.right
			return current

		current = self

		while current.parent != None:
			current = current.parent
			if current.val < self.val:
				return current
		return None

	def _replaceChild(self, n, m):
		if self.left == n:
			self.left = m
		elif self.right == n:
			self.right = m

	def min(self):
		current = self
		while current.parent != None and current.parent.right == current:
			current = current.parent
		while current.left != None:
			current = current.left
		return current
		
	def max(self):
		current = self
		while current.parent != None and current.parent.left == current:
			current = current.parent
		while current.right != None:
			current = current.right
		return current

	def inOrderTraverse(self):
		out = ''
		#Go left
		if self.left != None:
			out += self.left.inOrderTraverse()
		#Print self
		out += self.__repr__() + " "
		#Go right
		if self.right != None:
			out += self.right.inOrderTraverse()

		if self.parent == None:
			print(out)
		else:
			return out


	def delete(self, n):
		found = n
		if found != None:
			'''
				If no children, just delete

					*
					|
					0
				   /
				  *

				  Connect to parent if only one child

					*
					|
					0
				   / \
				  *   *

				  Find successor to node to be deleted, 
				  delete successor node and replace original node value with 
				  successor node value
			'''
			if found.left == None and found.right == None:
				if found.parent != None:
					found.parent._replaceChild(found, None)
				else:
					found.val = None
				found = None
			elif found.left != None and found.right == None and found.parent != None:
				if found.parent != None:
					found.parent._replaceChild(found, found.left)				
				found.left.parent = found.parent
				found = None
			elif found.right != None and found.left == None and found.parent != None:
				if found.parent != None:
					found.parent._replaceChild(found, found.right)
				found.right.parent = found.parent
				found = None
			else:
				successor = found.successor()
				found.val = successor.val
				self.delete(successor)




if __name__ == "__main__":
	A =[
		[32, 7, 17, 24, 75, 100, 111, 101, 102, 2, 3, 204, 55, 66, 60, 11, 33, 34 ],
		[7,56,88,64,667,97,986,5,44,768,547,876,767,222,333,444,555,434,91,723,575,845,253,111,20,672,785,693,822,389,797,123,4444,37,100,101,209,917,888,778,887,234,345,456,567,677,789,879,987,876,765,654,543,432,321,132],
		[1,2,3,4,5],
	]

	S = [
		[100, 66, 11, 32, 204, 2],

		[7, 88,456,987,666,797,243,222,111,100,5,876,777],
		[1,4,5,3,2],
	]


	for i in range(len(A)):
		#Build tree
		print("Building tree with {}".format(A[i]))
		t = bst(A[i][0])
		for ai in range(1, len(A[i])):
			t.insert(bst(A[i][ai]))

		#Find elements
		for f in S[i]:
			print("t.find({}) = {}".format(f, t.find(f)))

		#Get successor
		for s in S[i]:
			sf = t.find(s)
			if sf != None:
				print("t.successor({}) = {}".format(s, sf.successor()))
			else:
				print("t.successor({}) = {}".format(s, None))

		#Get predecessor
		for p in S[i]:
			pf = t.find(p)
			if pf != None:
				print("t.predecessor({}) = {}".format(p, pf.predecessor()))
			else:
				print("t.predecessor({}) = {}".format(p, None))

		#Traverse
		t.inOrderTraverse()
		print('min = {}'.format(t.min()))
		print('max = {}'.format(t.max()))

		#Delete elements
		for d in S[i]:
			df = t.find(d)
			if df != None:
				t.delete(df)
				print("t.delete({})".format(d))
			else:
				print("{} not found in t".format(d))

		#Traverse
		t.inOrderTraverse()







