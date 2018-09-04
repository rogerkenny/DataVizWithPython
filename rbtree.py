class node():
	def __init__(self, val, black=False, parent=None, left=None, right=None):
		self.val = val
		self.black = black
		self.parent = parent
		self.left = left
		self.right = right

	def isLeftChild(self):
		if self.parent == None:
			return False
		return self.parent.left == self

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

	def grandparent(self):
		if self.parent == None or self.parent.parent == None:
			return None
		return self.parent.parent

	def flipColor(self):
		self.black = not self.black

	def swapChild(self, n, x):
		if self.left == n:
			self.left = x
		else:
			self.right = x

	def successor(self, val):
		pass

	def predecessor(self, val):
		pass

	def __repr__(self):
		COLR = 'B' if self.black else 'R'
		out = "{}{}".format(COLR, self.val) if False else self.__str__()
		return out

	def __str__(self):
		COLR = '\33[90m' if self.black else '\033[91m'
		CEND = '\033[0m'
		return "{}{}{}".format(COLR, self.val, CEND)


class rbTree():
	def __init__(self):
		self.root = None
		self.sentinel = node('S', black=True)

	def insert(self, val):
		x = node(val, left=self.sentinel, right=self.sentinel)
		if self.root == None:
			x.black = True
			self.root = x
			return
		else:
			current = self.root
			while True:
				if current.val == val:
					return
				elif current.val > val:
					if current.left == self.sentinel:
						current.left = x
						x.parent = current
						break
					else:
						current = current.left
						continue
				elif current.val < val:
					if current.right == self.sentinel:
						current.right = x
						x.parent = current
						break
					else:
						current = current.right
						continue
			self.fixRedBlack(x)
		
	def fixRedBlack(self, n):
		# print("FIXREDBLACK\nn is {}".format(n))
		while n != self.root and n.parent.black != True:
			# if n.black:
			# 	return
			if n.parent == n.parent.parent.left:
				# parent is to the left
				# print("CASE A")
				u = n.parent.parent.right
				# print("u is {} and is right".format(u))
				if not u.black:
					# case 1 -> change the colors
					n.parent.black = True
					u.black = True
					if n.parent.parent != None:
						n.parent.parent.black = False
					# move x up the tree
					# print("CASE 1: n{} p{} u{}".format(n, p, u))
					n = n.parent.parent
				else:
					# uncle is black
					if n == n.parent.right:
						# and n is to the right
						# case 2 -> move n up and rotate
						n = n.parent
						self.rotateLeft(n)
					# case 3
					n.parent.black = True
					if n.parent.parent != None:
						n.parent.parent.black = False
						self.rotateRight(n.parent.parent)
			else:
				u = n.parent.parent.left
				if not u.black:
					# case 1 -> change the colors
					n.parent.black = True
					u.black = True
					if n.parent.parent != None:
						n.parent.parent.black = False
					# move x up the tree
					n = n.parent.parent
				else:
					# uncle is black
					if n == n.parent.left:
						# and n is to the right
						# case 2 -> move n up and rotate
						n = n.parent
						self.rotateRight(n)
					# case 3
					n.parent.black = True
					if n.parent.parent != None:
						n.parent.parent.black = False
						self.rotateLeft(n.parent.parent)
		self.root.black = True
		

	def delete(self, val):
		pass

	def find(self, val):
		current = self.root
		while True:
			if current.val == val:
				return current
			elif current.val < val:
				if current.right == self.sentinel:
					return None
				else:
					current = current.right
					continue
			elif current.val > val:
				if current.left == self.sentinel:
					return None
				else:
					current = current.left
					continue

	def rotateRight(self, n):
		if n == None:
			return
		l = n.left
		if l == self.sentinel:
			return
		p = n.parent
		if p != None:
			p.swapChild(n, l)
		else:
			self.root = l
		l.parent = p
		n.parent = l

		lr = l.right
		l.right = n
		n.left = lr
		if lr != None:
			lr.parent = n

	def rotateLeft(self, n):
		if n == None:
			return
		r = n.right
		if r == self.sentinel:
			return
		p = n.parent
		if p != None:
			p.swapChild(n, r)
		else:
			self.root = r
		r.parent = p
		n.parent = r

		rl = r.left
		r.left = n
		n.right = rl
		if rl != None:
			rl.parent = n

	def min(self):
		pass

	def max(self):
		pass

	def inOrderTraverse(self):
		def dp(x):
			out = ''
			if x != self.sentinel:
				out += dp(x.left)
				out += x.__repr__() + " "
				out += dp(x.right)
			return out
		return dp(self.root)

	def asciiTree(self):
		def dp(x):
			out = ''
			if x == None:
				return out
			leftConnector = '|' if (not x.isLeftChild() and x.parent != None) else ' '
			rightConnector = '|' if x.isLeftChild() else ' '
			prefix = ""
			if x.parent != None:
				prefix = "L-" if x.isLeftChild() else "R-"
			if x == self.sentinel:
				prefix = ""
			childPad = " " * (len(str(x.val)) + len(prefix))
			leftOut = dp(x.left)
			leftOut = [ "{}{}{}\n".format(leftConnector,childPad,l) for l in leftOut.split('\n') if l != '']
			out += ''.join(leftOut)
			out += prefix + x.__repr__() + '\n'
			rightOut = dp(x.right)
			rightOut = [ "{}{}{}\n".format(rightConnector,childPad,l) for l in rightOut.split('\n') if l != '']
			out += ''.join(rightOut)
			return out
		return dp(self.root)



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
			t.insert(A[i][ai])

		#Find elements
		for f in S[i]:
			print("t.find({}) = {}".format(f, t.find(f)))

		#Get successor
		# for s in S[i]:
		# 	sf = t.find(s)
		# 	if sf != None:
		# 		print("t.successor({}) = {}".format(s, sf.successor()))
		# 	else:
		# 		print("t.successor({}) = {}".format(s, None))

		#Get predecessor
		# for p in S[i]:
		# 	pf = t.find(p)
		# 	if pf != None:
		# 		print("t.predecessor({}) = {}".format(p, pf.predecessor()))
		# 	else:
		# 		print("t.predecessor({}) = {}".format(p, None))

		#Traverse
		print(t.inOrderTraverse())
		print(t.asciiTree())
		# print('min = {}'.format(t.min()))
		# print('max = {}'.format(t.max()))

		#Delete elements
		# for d in S[i]:
		# 	df = t.find(d)
		# 	if df != None:
		# 		t.delete(df)
		# 		print("t.delete({})".format(d))
		# 	else:
		# 		print("{} not found in t".format(d))

		#Traverse
		# t.inOrderTraverse()
		# t.asciiTree()
