# coding: utf-8
# coding: utf-8
import queue, sys, time

mobile = False

class Node:
	def __init__(self, data):
		self.data = data
		self.edges = []
		self.lastCost = 0
		self.cost = 0
		
	def connect(self, node):
		self.edges.append(node)

	def __lt__(self, other):
		return self.cost < other.cost if self.cost != other.cost else self.lastCost < other.lastCost
		
	def __sub__(self, other):
		return self.lastCost - other.lastCost
		
	def __add__(self, other):
		return self.lastCost + other.lastCost

class graph:
	def __init__(self):
		'''adjacency list'''
		self.nodes = []
		self.start = None
		self.end = None
		
	def makeFullyConnectedGrid(self, w=10, h=10):
		self.data = []
		for y in range(h):
			self.data.append([])
			for x in range(w):
				self.data[y].append(1)
		self.buildGraphFromData()
		
	def makeGraphFromFile(self, filename):
		f = open(filename, 'r')
		self.data = []
		li = 0
		for line in f:
			l = line.strip()
			if len(l) == 0:
				continue
			self.data.append([])
			for c in l:
				#print (c)
				if c.lower() in ['s', 'e']:
					self.data[li].append(c)
				else:
					self.data[li].append(int(c))
			li += 1
		f.close()
		#print(self.data)
		self.buildGraphFromData()
			
				
	def buildGraphFromData(self):
		self.nodes = []
		self.nodegrid = []
		for y, row in enumerate(self.data):
			self.nodegrid.append([])
			for x, cell in enumerate(row):
				self.nodegrid[y].append(None)
				'''Build nodes'''
				if str(self.data[y][x]).lower() == "s":
					node = Node((x,y,1)) # column, row, weight
					self.start = node
					self.nodes.append(node)
					self.nodegrid[y][x] = node

				elif str(self.data[y][x]).lower() == "e":
					node = Node((x,y,1)) # column, row, weight
					self.end = node
					self.nodes.append(node)
					self.nodegrid[y][x] = node

				elif self.data[y][x] > 0:
					node = Node((x,y,self.data[y][x])) # column, row, weight
					self.nodes.append(node)
					self.nodegrid[y][x] = node
					
		w = len(self.nodegrid[0])
		h = len(self.nodegrid)		
		for y, row in enumerate(self.nodegrid):
			for x, node in enumerate(row):
				'''connect nodes'''
				if node == None:
					continue
				dirs = [(0,-1),(1,0),(0,1),(-1,0)]
				for d in dirs:
					cx, cy = (x + d[0], y + d[1])
					if cx in range(w) and cy in range(h):
						if self.nodegrid[cy][cx] != None:
							node.connect(self.nodegrid[cy][cx])
							
	def __repr__(self):
		rep = ''
		for y, row in enumerate(self.nodegrid):
			for x, node in enumerate(row):
				if node == None:
					rep += 'X'
					continue
				# rep+= '{}'.format(len(node.edges)) # num of edges
				# rep += '-'
				rep += '{}'.format(node.data[2]) # weight
			rep += '\n'
		return rep 
	
					
class pathFinder:
	def __init__(self, graph, start=None, end=None):
		self.graph = graph
		self.start = start if start!= None else graph.start
		self.end = end if start!= None else graph.end
		if self.start == None or self.end == None:
			raise ValueError
		self.found = False
		self.path = self.greedy()
		self.drawFrame()
		print('Greedy cost = {}\n'.format(len(self.path) ) )
		self.path = self.dijkstra()
		self.drawFrame()
		print('Dijkstra cost = {}\n'.format(len(self.path)))
		self.path = self.astar()
		self.drawFrame()
		print('A* cost = {}\n'.format(len(self.path)))
		
	def dijkstra(self):
		if not mobile:
			print("\n" * len(self.graph.nodegrid))
		self.found = False
		q = queue.PriorityQueue()
		self.cameFrom = {} 
		self.costSoFar = {}
		self.current = self.start
		q.put( self.start)
		self.costSoFar[self.start] = 0
		while not q.empty():
			if not mobile:
				self.drawFrame()
			self.current = q.get()
			if self.current == self.end:
				path = [self.current]
				while self.current is not self.start:
					self.current = self.cameFrom[self.current]
					path.append(self.current)
				self.found = True
				return path
			for a in self.current.edges:
				new_cost = self.costSoFar[self.current] + self.current.data[2]
				if a not in self.costSoFar or new_cost < self.costSoFar[a]:
					self.costSoFar[a] = new_cost
					a.lastCost = new_cost
					q.put( a)
					self.cameFrom[a] = self.current
					
	def astar(self):
		if not mobile:
			print("\n" * len(self.graph.nodegrid))
		self.found = False
		q = queue.PriorityQueue()
		self.cameFrom = {} 
		self.costSoFar = {}
		self.current = self.start
		q.put( self.start)
		self.costSoFar[self.start] = 0
		while not q.empty():
			if not mobile:
				self.drawFrame()
			self.current = q.get()
			if self.current == self.end:
				path = [self.current]
				while self.current is not self.start:
					self.current = self.cameFrom[self.current]
					path.append(self.current)
				self.found = True
				return path
			for a in self.current.edges:
				new_cost = self.costSoFar[self.current] + a.data[2] + self.h(a)
				if a not in self.costSoFar or new_cost < self.costSoFar[a]:
					self.costSoFar[a] = new_cost
					a.lastCost = new_cost
					a.cost = a.data[2] + self.h(a)
					q.put(a)
					self.cameFrom[a] = self.current

	def greedy(self):
		if not mobile:
			print("\n" * len(self.graph.nodegrid))
		self.found = False
		q = queue.PriorityQueue()
		self.cameFrom = {} 
		self.costSoFar = {}
		self.current = self.start
		q.put( self.start)
		self.costSoFar[self.start] = 0
		while not q.empty():
			if not mobile:
				self.drawFrame()
			self.current = q.get()
			if self.current == self.end:
				path = [self.current]
				while self.current is not self.start:
					self.current = self.cameFrom[self.current]
					path.append(self.current)
				self.found = True
				return path
			for a in self.current.edges:
				new_cost = self.h(a)
				if a not in self.costSoFar:
					self.costSoFar[a] = new_cost
					a.lastCost = new_cost
					q.put(a)
					self.cameFrom[a] = self.current
					
	def h(self, n):
		e = self.end
		return abs(e.data[0] - n.data[0]) + abs(e.data[1] - n.data[1])

	def drawFrame(self):
		if not mobile:
			sys.stdout.write(u"\u001b[1000D") # Move left
			sys.stdout.write(u"\u001b[" + str((len(self.graph.nodegrid) + 2)) + "A") #move up
		print(self.__repr__())
		time.sleep(0.01)


	def __repr__(self):
		g = [ [ _c(j) for j in list(line) if j != "\n" ] for line in self.graph.__repr__().split("\n")]

		for n in self.costSoFar.keys():
			g[n.data[1]][n.data[0]] = c['yellow'] + "." + c['r']

		g[self.current.data[1]][self.current.data[0]] = "%"

		# print (g)
		if self.found:
			for p in self.path:
				g[p.data[1]][p.data[0]] = c['black'] + '*' + c['r']

		g[self.start.data[1]][self.start.data[0]] = c['green'] + "S" + c["r"]
		g[self.end.data[1]][self.end.data[0]] = c['red'] + "E" + c["r"]


		s = ''
		for r in g:
			s+= ''.join(r)
			s+= '\n'

		return s[:-2] if mobile else s


def _c(si):
	if mobile:
		return si

	if si in ["X","0"]:
		return c["blackB"] + si + c["r"]

	if si in ['E', 'S']:
		si = "1"

	i = int(si) 


	return c[bkcol[i % len(bkcol)]] + si + c["r"]




bkcol = ["yellow", "mustard", "red", "green", "pink"]

c = {
		"yellow" : "",
		"blackB" : "",
		"black"	: "",
		"red" : "",
		"green" : "",
		"r" : "",
		"r2" : "",
		"mustard" : "",
		"pink" : ""
	}

if not mobile:
	c = {
		"yellow" : "\033[93m",
		"blackB" : "\u001b[40m",
		"black"	: "\u001b[30m",
		"red" : "\u001b[31m",
		"green" : "\u001b[32m",
		"r" : "\u001b[0m",
		"r2" : "\033[0m",
		"mustard" : "\033[33m",
		"pink" : "\033[35m"
	}
		
	

g = graph()

if not mobile:
	g.makeGraphFromFile('graphLayout.txt')
else:
	g.makeGraphFromFile('graphLayoutPh.txt')

# print( g)

# p = pathFinder(g, g.nodegrid[10][4], g.nodegrid[10][40])
p = pathFinder(g)
# print(p)

		
