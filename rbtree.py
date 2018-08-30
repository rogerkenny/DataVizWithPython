class node():
	def __init__(self, val, black=False, parent=None, left=None, right=None):
		self.val = val
		self.black = black
		self.parent = parent
		self.left = left
		self.right = right

	def sibling(self):
		if self.parent == None:
			return None
		if self.parent.left == self:
			return self.parent.right
		else:
			return self.parent.left

	def uncle(self):
		if self.parent == None:
			return None
		return self.parent.sibling()

	def flipColor(self):
		self.black = not self.black


class rbTree():
	def __init__(self):
		self.root = None

	def insert(self, val):
		x = node(val)
		if self.root == None:
			x.flipColor()
			self.root = x
			return
		else:
			current = self.root
			while True:
				if current.val == val:
					return
				elif current.val > val:
					if current.left == None:
						current.left = x
						x.parent = current
						self.fixRedBlack(x)
						return
					else:
						current = current.left
						continue
				elif current.val < val:
					if current.right == None:
						current.right = x
						x.parent = current
						self.fixRedBlack(x)
						return
					else:
						current = current.right
						continue

	



	def fixRedBlack(self, n):
		pass

	def delete(self, val):
		pass

	def find(self, val):
		pass

	def rotateLeft(self, n):
		pass

	def rotateRight(self, n):
		pass

	def successor(self, val):
		pass

	def predecessor(self, val):
		pass

	def min(self):
		pass

	def max(self):
		pass

	def inOrderTraverse(self):
		pass

	def asciiTree(self):
		pass






if __name__ == "__main__":
	A =[
		[32, 7, 17, 24, 75, 100, 111, 101, 102, 2, 3, 204, 55, 66, 60, 11, 33, 34 ],
		[7,56,88,64,667,97,986,5,44,768,547,876,767,222,333,444,555,434,91,723,575,845,253,111,20,672,785,693,822,389,797,123,4444,37,100,101,209,917,888,778,887,234,345,456,567,677,789,879,987,876,765,654,543,432,321,132],
		[1,2,3,4,5],
	]

	R = [
		[],
		[],
		[]
	]

	S = [
		[100, 66, 11, 32, 204, 2],
		[7, 88,456,987,666,797,243,222,111,100,5,876,777],
		[1,4,5,3,2],
	]


	for i in range(len(A)):
		#Build tree
		print("Building tree with {}".format(A[i]))
		t = rbTree()
		for ai in range(0, len(A[i])):
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
		t.asciiTree()
		print('min = {}'.format(t.min()))
		print('max = {}'.format(t.max()))

		#Rotate
		for r in R[i]:
			rf = t.find(r[0])
			if rf != None:
				if r[1] == 'R':
					rf.rotateRight()
				else:
					rf.rotateLeft()
				t.asciiTree()

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
		t.asciiTree()
