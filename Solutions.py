
def plusOne( A):
	print(A)
	sa = [str(a) for a in A]
	x = "".join(sa)
	x = int(x)
	print(x)
	x += 1
	x = str(x)
	return list(x)

# print(plusOne([0]))

# def repeatedNumber(A):
# 	'''CUTE BUT DOESN'T WORK'''
# 	a = list(A)
# 	print("len a = ", len(a))
# 	a.sort()
# 	third = len(a) // 3
# 	'''Check the thirds'''
# 	for i in range(3):
# 		firstI = i * third
# 		rightI = (i + 1) * third - 1

# 		print(firstI, rightI)

# 		first = a[firstI]
# 		right = a[rightI] #? may not be correct
# 		extra = a[rightI + 1] if i < 2 else a[firstI - 1]
# 		if first == right and first == extra:
# 			return first
# 	return -1

def repeatedNumberB(A):
	a = list(A)
	third = len(a)/3
	#Keep track of the appearances of values
	candidates = dict() 
	#Hold the most frequent values
	scratch = set()
	#Previous 3 values
	prev = set()
	#Choose 3 at a time. 
	#If a value appears 1/3 of the array, 
	#there should be a 1 in 3 chance of picking it
	for i in range(0, len(A), 3):
		#Next 3 values
		next3 = set()
		for j in range(i, i+3):
			if j > len(a)-1:
				break
			current = a[j]
			#count appearance 
			if current in candidates:
				candidates[current] += 1
			else: 
				candidates[current] = 1
			#check if already > third
			if candidates[current] > third:
				return current
			next3.add(current)
		#Fill scratch with most common occurences by &ing and |ing sets 
		if len(prev) == 0:
			prev = next3
			scratch = scratch | next3
		else:
			scratch = scratch | (prev & next3)
	
	for c in scratch:
		if candidates[c] > third:
			return c
			
	return -1


A = [ 1000587, 1000280, 1000777, 1000367, 1000313, 1000669, 1000389, 1000553, 1000475, 1000822, 1000795, 1000367, 1000369, 1000014, 1000967, 1000407, 1000597, 1000943, 1000897, 1000367, 1000698, 1000367, 1000367, 1000367, 1000237, 1000501, 1000249, 1000090, 1000485, 1000621, 1000808, 1000041, 1000103, 1000367, 1000492, 1000367, 1000577, 1000885, 1000367, 1000295, 1000367, 1000496, 1000367, 1000675, 1000509, 1000367, 1000367, 1000284, 1000349, 1000367, 1000801, 1000367, 1000106, 1000367, 1000367, 1000367, 1000776, 1000077, 1000604, 1000318, 1000367, 1000367, 1000367, 1000925, 1000367, 1000367, 1000367, 1000949, 1000367, 1000367, 1000379, 1000644, 1000519, 1000367, 1000702, 1000367, 1000915, 1000365, 1000739, 1000367, 1000367, 1000766, 1000367, 1000618, 1000248, 1000367, 1000367, 1000246, 1000318, 1000870, 1000367, 1000296, 1000367, 1000420, 1000644, 1000807, 1000534, 1000265, 1000981, 1000367, 1000446, 1000859, 1000217, 1000261, 1000207, 1000367, 1000367, 1000040, 1000827, 1000286, 1000910, 1000575, 1000367, 1000367, 1000363, 1000882, 1000799, 1000697, 1000367, 1000628, 1000367, 1000659, 1000838, 1000627, 1000603, 1000671, 1000280, 1000843, 1000367, 1000666, 1000367, 1000367, 1000299, 1000315, 1000764, 1000280, 1000921, 1000634, 1000634, 1000145, 1000367, 1000367, 1000367, 1000409, 1000367, 1000752, 1000448, 1000367, 1000973, 1000944, 1000679, 1000367, 1000367, 1000465, 1000367, 1000139, 1000481, 1000927, 1000235, 1000839, 1000099, 1000367, 1000923, 1000367, 1000367, 1000604, 1000807, 1000367, 1000477, 1000367, 1000367, 1000567, 1000156, 1000243, 1000128, 1000405, 1000367, 1000591, 1000785, 1000469, 1000367, 1000789, 1000121, 1000785, 1000710, 1000079, 1000367, 1000587, 1000507, 1000897, 1000857, 1000161, 1000367, 1000367, 1000610, 1000367, 1000664, 1000863, 1000367, 1000068, 1000031, 1000736, 1000367, 1000367, 1000367, 1000215, 1000367, 1000448, 1000233, 1000661, 1000367, 1000095, 1000604, 1000367, 1000481, 1000385, 1000367, 1000367, 1000312, 1000367, 1000945, 1000357, 1000889, 1000189, 1000106, 1000367, 1000344, 1000231, 1000767, 1000178, 1000012, 1000953, 1000367, 1000201, 1000367, 1000173, 1000019, 1000106, 1000367, 1000367, 1000367, 1000555, 1000367, 1000585, 1000094, 1000120, 1000851, 1000746, 1000367, 1000367, 1000540, 1000232, 1000367, 1000619, 1000367, 1000969, 1000842, 1000367, 1000926, 1000790, 1000058, 1000454, 1000737, 1000883, 1000521, 1000367, 1000367, 1000367, 1000413, 1000367, 1000367, 1000367, 1000619, 1000722, 1000367, 1000367, 1000849, 1000367, 1000220, 1000948, 1000659, 1000168, 1000673, 1000834, 1000367, 1000452, 1000548, 1000306, 1000367, 1000099, 1000051, 1000062, 1000868, 1000828, 1000137, 1000367, 1000189, 1000400, 1000337, 1000367, 1000687, 1000863, 1000893, 1000429, 1000344, 1000367, 1000796, 1000991, 1000471, 1000131, 1000258, 1000589, 1000367, 1000367, 1000367, 1000455, 1000369, 1000367, 1000367, 1000367, 1000672, 1000022, 1000367, 1000367, 1000076, 1000036, 1000367, 1000153, 1000461, 1000367, 1000722, 1000725, 1000367, 1000367, 1000591, 1000367, 1000901, 1000213, 1000381, 1000350, 1000905, 1000154, 1000006, 1000367, 1000367, 1000569, 1000405, 1000612, 1000618, 1000367, 1000164, 1000015, 1000476, 1000037, 1000367, 1000695, 1000226, 1000925, 1000367, 1000047, 1000937, 1000367, 1000947, 1000871, 1000609, 1000551, 1000367, 1000648, 1000880, 1000014, 1000367, 1000367, 1000473, 1000459, 1000367, 1000367, 1000367, 1000253, 1000367, 1000779, 1000993, 1000367, 1000871, 1000855, 1000367, 1000879, 1000809, 1000996, 1000592, 1000324, 1000367, 1000367, 1000602, 1000663, 1000537, 1000809, 1000395, 1000367, 1000970, 1000878, 1000462, 1000441, 1000367, 1000102, 1000023, 1000367, 1000367, 1000724, 1000367, 1000801, 1000617, 1000367, 1000350, 1000413, 1000056, 1000853, 1000332, 1000487, 1000456, 1000027, 1000367, 1000530, 1000367, 1000276, 1000475, 1000367, 1000279, 1000367, 1000367, 1000678, 1000367, 1000195, 1000396, 1000367, 1000367, 1000076, 1000684, 1000892, 1000993, 1000895, 1000918, 1000987, 1000855, 1000367, 1000367, 1000493, 1000275, 1000367, 1000367, 1000487, 1000464, 1000798, 1000536, 1000367, 1000370, 1000712, 1000909, 1000026, 1000367, 1000726, 1000367, 1000198, 1000069, 1000063, 1000471, 1000275, 1000367, 1000801, 1000367, 1000283, 1000367, 1000367, 1000366, 1000367 ]
B = [ 1000274, 1000802, 1000914, 1000847, 1000073, 1000562, 1000741, 1000802, 1000965, 1000371, 1000406, 1000441, 1000179, 1000802, 1000552, 1000802, 1000100, 1000724, 1000024, 1000134, 1000313, 1000802, 1000977, 1000777, 1000206, 1000412, 1000802, 1000570, 1000802, 1000518, 1000691, 1000959, 1000903, 1000802, 1000802, 1000273, 1000802, 1000802, 1000265, 1000706, 1000677, 1000802, 1000843, 1000802, 1000061, 1000802, 1000802, 1000975, 1000403, 1000150, 1000959, 1000889, 1000177, 1000416, 1000491, 1000177, 1000807, 1000989, 1000489, 1000447, 1000802, 1000860, 1000104, 1000802, 1000570, 1000015, 1000802, 1000802, 1000593, 1000802, 1000802, 1000326, 1000802, 1000802, 1000120, 1000772, 1000965, 1000802, 1000887, 1000802, 1000567, 1000973, 1000577, 1000820, 1000922, 1000802, 1000982, 1000525, 1000369, 1000829, 1000740, 1000159, 1000909, 1000510, 1000402, 1000802, 1000802, 1000239, 1000247, 1000328, 1000427, 1000802, 1000519, 1000296, 1000114, 1000149, 1000802, 1000802, 1000107, 1000841, 1000017, 1000909, 1000192, 1000425, 1000088, 1000077, 1000506, 1000163, 1000465, 1000626, 1000371, 1000802, 1000179, 1000306, 1000159, 1000802, 1000802, 1000848, 1000138, 1000306, 1000802, 1000881, 1000828, 1000802, 1000008, 1000802, 1000456, 1000802, 1000880, 1000579, 1000434, 1000163, 1000188, 1000802, 1000802, 1000231, 1000945, 1000802, 1000070, 1000727, 1000802, 1000802, 1000802, 1000051, 1000644, 1000802, 1000802, 1000057, 1000967, 1000802, 1000802, 1000366, 1000802, 1000485, 1000802, 1000061, 1000212, 1000192, 1000577, 1000559, 1000802, 1000189, 1000802, 1000802, 1000107, 1000177, 1000011, 1000802, 1000987, 1000400, 1000802, 1000402, 1000024, 1000009, 1000118, 1000046, 1000349, 1000250, 1000282, 1000138, 1000405, 1000295, 1000802, 1000878, 1000166, 1000802, 1000135, 1000005, 1000723, 1000491, 1000802, 1000802, 1000802, 1000802, 1000786, 1000306, 1000802, 1000802, 1000802, 1000639, 1000683, 1000880, 1000329, 1000408, 1000822, 1000947, 1000802, 1000455, 1000037, 1000311, 1000802, 1000802, 1000339, 1000802, 1000519, 1000401, 1000802, 1000256, 1000802, 1000802, 1000503, 1000802, 1000787, 1000802, 1000802, 1000384, 1000456, 1000845, 1000802, 1000802, 1000000, 1000213, 1000629, 1000802, 1000226, 1000802, 1000802, 1000107, 1000100, 1000802, 1000587, 1000882, 1000049, 1000623, 1000802, 1000178, 1000788, 1000648, 1000802, 1000567, 1000802, 1000802, 1000802, 1000085, 1000109, 1000965, 1000353, 1000802, 1000802, 1000802, 1000982, 1000663, 1000829, 1000578, 1000753, 1000802, 1000802, 1000529, 1000060, 1000047, 1000802, 1000750, 1000780, 1000277, 1000802, 1000751, 1000590, 1000802, 1000953, 1000240, 1000218, 1000659, 1000802, 1000001, 1000766, 1000802, 1000508, 1000802, 1000802, 1000802, 1000028, 1000802, 1000493, 1000077, 1000427, 1000505, 1000752, 1000802, 1000747, 1000126, 1000269, 1000297, 1000394, 1000257, 1000708, 1000802, 1000802, 1000697, 1000802, 1000802, 1000802, 1000921, 1000559, 1000450, 1000206, 1000802, 1000802, 1000149, 1000031, 1000866, 1000721, 1000497, 1000654, 1000057, 1000802, 1000130, 1000523, 1000577, 1000750, 1000536, 1000339, 1000796, 1000802, 1000802, 1000197, 1000584, 1000939, 1000802, 1000633, 1000553, 1000124, 1000086, 1000619, 1000802, 1000415, 1000802, 1000125, 1000802, 1000104, 1000348, 1000464, 1000187, 1000887, 1000369, 1000281, 1000802, 1000802, 1000526, 1000685, 1000029, 1000922, 1000191, 1000802, 1000802, 1000802, 1000298, 1000802, 1000176, 1000295, 1000802, 1000802, 1000238, 1000802, 1000802, 1000314, 1000303, 1000802, 1000698, 1000309, 1000677, 1000606, 1000802, 1000701, 1000898, 1000579, 1000990, 1000513, 1000435, 1000192, 1000960, 1000324, 1000509, 1000906, 1000802, 1000492, 1000705, 1000641, 1000479, 1000662, 1000642, 1000791, 1000942, 1000802, 1000802, 1000100, 1000296, 1000802, 1000802, 1000533, 1000802, 1000038, 1000802, 1000254, 1000802, 1000802, 1000802, 1000802, 1000393, 1000802, 1000435, 1000484, 1000802, 1000847, 1000802, 1000360, 1000961, 1000544, 1000914, 1000802, 1000802, 1000663, 1000802, 1000802, 1000519, 1000802, 1000928, 1000802, 1000802, 1000802, 1000802, 1000258, 1000108, 1000544, 1000802, 1000169, 1000097, 1000802, 1000306, 1000977, 1000802, 1000153, 1000802, 1000802, 1000039, 1000099, 1000802, 1000468, 1000862, 1000802, 1000802, 1000802, 1000068, 1000802, 1000161, 1000179, 1000710, 1000802, 1000802, 1000802, 1000802, 1000540, 1000802, 1000115, 1000802, 1000802, 1000089, 1000802, 1000798, 1000802, 1000802, 1000544, 1000979, 1000850, 1000085, 1000197, 1000802, 1000802, 1000031, 1000704, 1000515, 1000802, 1000198, 1000382, 1000597, 1000613, 1000857, 1000798, 1000319, 1000266, 1000154, 1000753, 1000017, 1000004, 1000802 ]
C = [ 1000545, 1000038, 1000647, 1000038, 1000562, 1000038, 1000586, 1000487, 1000951, 1000226, 1000038, 1000145, 1000038, 1000761, 1000196, 1000038, 1000821, 1000829, 1000038, 1000570, 1000846, 1000038, 1000178, 1001000, 1000038, 1000568, 1000278, 1000734, 1000048, 1000038, 1000002, 1000271, 1000388, 1000315, 1000816, 1000038, 1000038, 1000846, 1000305, 1000853, 1000383, 1000116, 1000797, 1000279, 1000038, 1000038, 1000049, 1000108, 1000789, 1000240, 1000201, 1000506, 1000429, 1000857, 1000649, 1000898, 1000211, 1000000, 1000178, 1000038, 1000569, 1000695, 1000451, 1000159, 1000038, 1000038, 1000038, 1000129, 1000038, 1000038, 1000904, 1000038, 1000038, 1000902, 1000525, 1000038, 1000166, 1000038, 1000765, 1000038, 1000561, 1000417, 1000523, 1000668, 1000296, 1000038, 1000038, 1000038, 1000461, 1000654, 1000924, 1000985, 1000038, 1000426, 1000038, 1000038, 1000038, 1000904, 1000775, 1000148, 1000961, 1000038, 1000038, 1000038, 1000833, 1000332, 1000038, 1000038, 1000512, 1000322, 1000592, 1000524, 1000788, 1000057, 1000497, 1000625, 1000599, 1000484, 1000038, 1000747, 1000457, 1000111, 1000038, 1000038, 1000493, 1000287, 1000007, 1000695, 1000344, 1000098, 1000038, 1000191, 1000038, 1000576, 1000481, 1000488, 1000199, 1000038, 1000663, 1000176, 1000038, 1000521, 1000721, 1000728, 1000247, 1000038, 1000038, 1000460, 1000644, 1000038, 1000497, 1000966, 1000431, 1000038, 1000975, 1000063, 1000580, 1000669, 1000038, 1000038, 1000492, 1000038, 1000038, 1000529, 1000553, 1000333, 1000038, 1000341, 1000569, 1000862, 1000017, 1000532, 1000571, 1000508, 1000402, 1000285, 1000611, 1000210, 1000646, 1000110, 1000038, 1000553, 1000273, 1000729, 1000038, 1000038, 1000720, 1000400, 1000038, 1000983, 1000038, 1000766, 1000038, 1000180, 1000494, 1000765, 1000136, 1000038, 1000029, 1000246, 1000991, 1000038, 1000759, 1000038, 1000038, 1000045, 1000038, 1000648, 1000038, 1000038, 1000694, 1000914, 1000990, 1000038, 1000038, 1000758, 1000435, 1000038, 1000554, 1000038, 1000452, 1000156, 1000038, 1000322, 1000828, 1000868, 1000038, 1000973, 1000991, 1000464, 1000294, 1000633, 1000038, 1000582, 1000229, 1000285, 1000038, 1000038, 1000086, 1000038, 1000989, 1000038, 1000038, 1000157, 1000307, 1000369, 1000300, 1000038, 1000038, 1000038, 1000244, 1000038, 1000038, 1000222, 1000458, 1000038, 1000523, 1000434, 1000316, 1000038, 1000256, 1000038, 1000695, 1000038, 1000469 ]


print(repeatedNumberB(C))

A = [ -846930886, -1714636915, 424238335, -1649760492 ]

def maxset(A):
	'''
	Build list of subarrays like this:
	[sum, length, start]
	
	sort list by sum, then length, then start
	'''
	setsOfSubArrays = []
	for i in range(len(A)):
		if A[i] < 0:
			setsOfSubArrays.append([0,0,i+1])
			continue
		if len(setsOfSubArrays) == 0:
			setsOfSubArrays.append([0,0,i])
		setsOfSubArrays[-1][0] += A[i]
		setsOfSubArrays[-1][1] += 1
	
	setsOfSubArrays.sort()
	print(setsOfSubArrays)
	answ = setsOfSubArrays[-1]
	return A[answ[2]: answ[2] + answ[1]]

print(maxset(A))


class Pascal:
	# @param A : integer
	# @return a list of list of integers
	def generate(self, A):
		self.facmemo = {}
		triangle = []
		for n in range(A):
			row = []
			for k in range(n + 1):
				p = int(self._fac(n)/(self._fac(k)*self._fac(n-k)))
				row.append(p)
			triangle.append(row)
		return triangle

	def show(self, A):
		p = self.generate(A)
		for r in p:
			print(r)
				
				
	def _fac(self, x):
		if x == 0:
			return 1
		
		if x in self.facmemo:
			return self.facmemo[x]
			
		fac = x
		fac *= self._fac(x - 1)
			
		self.facmemo[x] = fac
		return fac

pascal = Pascal()
pascal.show(20)

class MatRot:
	# @param A : list of list of integers
	# @return the same list modified
	def rotate(self, A):
		half = len(A)//2
		for row in range(half):
			print("r", row)
			for c in range(row,len(A[row]) - 1 - row):
				print("c", c)
				self.rot(A, (row,c), (c, len(A)-row -1), (len(A)-row -1, len(A[row]) - c-1), (len(A) - c-1, row))
		
		return A
		
		
	def rot(self, A, a, b, c, d):
		temp = A[a[0]][a[1]]
		A[a[0]][a[1]] = A[d[0]][d[1]]
		A[d[0]][d[1]] = A[c[0]][c[1]]
		A[c[0]][c[1]] = A[b[0]][b[1]]
		A[b[0]][b[1]] = temp

	def show(self, A):
		out = self.rotate(A)
		for r in out:
			print(r)
		print("\n")


matrot = MatRot()
M = [
	[11,12,13,14],
	[15,16,17,18],
	[19,20,21,22],
	[23,24,25,26]
]

M = [
	[11,12,13,14,15],
	[16,17,18,19,20],
	[21,22,23,24,25],
	[26,27,28,29,30],
	[31,32,33,34,35]
]
for r in M:
	print(r)
print("\n")
matrot.show(M)


class HammingDistance:
	# @param A : tuple of integers
	# @return an integer
	def hammingDistance(self, A):
		memo = {}
		hamSum = 0
		for e in A:
			for f in A:
				hamSum += self.hd(e, f, memo)
				print(e, f, self.hd(e, f, memo), hamSum)
			print("\n")
				
		return hamSum
	
	def hd(self, x, y, memo):
		key = str(x) + "+" + str(y)
		if key in memo:
			return memo[key]
		xor = x^y
		# h = 0
		# for b in range(xor.bit_length()):
		# 	xor >>= 1
		# 	if xor & 1 == 1:
		# 		h += 1
		h = bin(xor).count("1")
		memo[key] = h
		return h

A = [ 96, 96, 7, 81, 2, 13 ]
hd = HammingDistance()
print(hd.hammingDistance(A))

class UniquePaths:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def uniquePaths(self, A, B):
		memo = {}
		return self.pathsFrom( A, B, 0, 0, memo)
		
	def pathsFrom(self, A, B, r, c, memo):
		if r >= A or c >= B:
			return 0
		if r == A-1 or c == B-1:
			return 1
		key = str(r) + "-" + str(c)
		if key in memo:
			return memo[key]
			
		paths = self.pathsFrom(A,B,r+1,c,memo) + self.pathsFrom(A,B,r,c+1,memo)
		memo[key] = paths
		return paths



def arrange(A):
	print('A len = ', len(A))
	shift = 1
	while (1 << shift) < len(A):
		shift += 1
	print('shift = ', shift )

	print([ '{0:b}'.format(n) for n in A])
	
	''' Shift all values '''
	for i in range(len(A)):
		A[i] = A[i] << shift
	
	print('After shift')
	print([ '{0:b}'.format(n) for n in A])

	''' Add new values '''
	for i in range(len(A)):
		A[i] += A[ (A[i] >> shift) ] >> shift

	print('After add')
	print([ '{0:b}'.format(n) for n in A])
		
	''' Mask to remove old values '''
	mask = 0
	while shift > 0:
		shift -= 1
		mask += 1 << shift

	print('mask = ', '{0:b}'.format(mask))
	for i in range(len(A)):
		A[i] = A[i] & mask

	print('After mask')
	print([ '{0:b}'.format(n) for n in A])


				
A = [ 4, 0, 2, 1, 3 ]

print('Before arrange:', A)
arrange(A)
print('After arrange', A)


def lenNlessThanK( A, B, C):
	if B > len(str(C)):
		return 0
		
	numPossible = 0
	memo = {}
	
	comb = []
	def recurse(A, digitsleft, memo, comb):
		if digitsleft == 0:
			return []
		comb = []
		if digitsleft in memo:
			return memo[digitsleft]
		for d in A:
			rem = recurse(A, digitsleft - 1, memo, comb)
			if len(rem) == 0:
				comb.append(str(d))
			else:
				for c in rem:
					comb.append(str(d) + c)
		memo[digitsleft] = comb
		return comb
		
	combinations = recurse(A, B, memo, comb)
	# print(combinations)
	for c in combinations:
		if len(c) > 1 and c[0] == '0':
			continue
		if int(c) < C:
			# print(c, numPossible)
			numPossible += 1
			
	return numPossible

print("\n\n")

A = [ 0, 1, 2, 3, 4, 5, 7, 8, 9 ]
B = 5
C = 51822
print(lenNlessThanK(A, B, C))

A = [ 0, 1, 2, 3, 4, 5, 7, 8, 9 ]
B = 4
C = 9999
print(lenNlessThanK(A, B, C))

def lenNlessThanKCount( A, B, C ):
	if B > len(str(C)):
		return 0
	numPossible = 0

	def recurse(digitsleft, acc=0):
		if digitsleft == 0:
			# print(acc)
			return 1 if acc < C else 0

		numPossible = 0
		for d in A:
			if digitsleft == B and d == 0 and B != 1:
				continue
			if digitsleft == B and d * 10**(digitsleft-1) > C:
				continue
			numPossible += recurse( digitsleft - 1, acc + d * 10**(digitsleft-1))
		return numPossible
		
	numPossible = recurse(B, 0)
			
	return numPossible


print("\n\n")

A = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
B = 5
C = 51822
print(lenNlessThanKCount(A, B, C))

A = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
B = 4
C = 9999
print(lenNlessThanKCount(A, B, C))

def lenNlessThanKDigits( A, B, C ):
	if B > len(str(C)):
		return 0
	numPossible = 0

	def recurse(digitsleft, acc=0):
		if digitsleft == 0:
			# print(acc)
			return 1 if acc < C else 0

		numPossible = 0
		for d in A:
			if digitsleft == B and d == 0 and B != 1:
				continue
			if digitsleft == B and d * 10**(digitsleft-1) > C:
				continue
			numPossible += recurse( digitsleft - 1, acc + d * 10**(digitsleft-1))
		return numPossible
		
	numPossible = recurse(B, 0)
			
	return numPossible

def hammingDistance( A ):
	memo = {}
	hamTotal = 0
	
	def _k(a, b):
		low = min(a, b)
		hi = max(a, b)
		return '{}+{}'.format(low,hi)
		
	def ham(a, b):
		# s = '{0:b}'.format(a ^ b)
		# return len([n for n in list(s) if n == '1'])
		s = a ^ b
		count = 0
		while (s):
			count += s & 1
			s >>= 1
		return count

		
	for a in A:
		for b in A:
			key = _k(a, b)
			if key in memo:
				hamTotal += memo[key]
				continue
			hamTotal += ham(a, b)
			
	return hamTotal


def hammingDistanceWLookup(self, A):
	memo = {}
	hamTotal = 0
	
	def _k(a, b):
		low = min(a, b)
		hi = max(a, b)
		return '{}+{}'.format(low,hi)
		
	'''Really neat solution for counting bits in O(1) using a lookup table'''
	'''From http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetNaive'''
	def bitSet(n):
		count = 0
		while (n):
			count += n & 1
			n >>= 1
		return count
		
	bitSetLookup = []
	for i in range(256):
		bitSetLookup.append(bitSet(i))
		
	def ham(a, b):
		s = a ^ b
		c = bitSetLookup[s & 0xff] 
		c += bitSetLookup[(s >> 8) & 0xff]
		c += bitSetLookup[(s >> 16) & 0xff]
		c += bitSetLookup[(s >> 24) & 0xff]
		return c
		
	for a in A:
		for b in A:
			key = _k(a, b)
			if key in memo:
				hamTotal += memo[key]
				continue
			hamTotal += ham(a, b)
			
	return hamTotal % 1000000007



def sqrtBin(A):
	'''Binary search for squareroot
	
	test = Try half way point.
	
	If too big, try half between test and start ( 0 at begin )
	If too small try half between test and end ( A at begin )
	If found or start == end return test
	
	'''
	start, end = 0, A
	test = 0
	while start < end:
		test = (start + end) // 2
		test2 = test * test
		# print("s: {}, e: {}, t: {}, t2: {}".format(start, end, test, test2))
		if test2 == A:
			return test
		elif test2 > A:
			end = test - 1
		elif test2 < A:
			start = test + 1
	return start if (start * start) <= A else start - 1

A = [100120, 256, 25, 9, 6, 2, 0]
# A = [100120]

for a in A:
	print('sqrtBin of ', a, ' : ', sqrtBin(a))
	print('sqrt of ', a, ' : ', a**0.5)


def sqrtBinFloat(A):
	'''Binary search for squareroot
	
	test = Try half way point.
	
	If too big, try half between test and start ( 0 at begin )
	If too small try half between test and end ( A at begin )
	If found or start == end return test
	
	'''
	eps = 0.000000000001
	start, end = 0.0, float(A)
	test = 0.0
	while (end - start) > eps:
		step = (end - start)*0.01
		test = (start + end) / 2
		test2 = test * test
		# print("s: {}, e: {}, t: {}, t2: {}".format(start, end, test, test2))
		if test2 == A:
			return test
		elif test2 > A:
			end = test - step
		elif test2 < A:
			start = test + step
	return (start + end) / 2

A = [100120, 256, 25, 9, 6, 2, 0]
# A = [100120]

for a in A:
	a2 = sqrtBinFloat(a)
	a05 = a**0.5
	print('sqrtBinFloat of ', a, ' : ', a2)
	print('sqrt of ', a, ' : ', a05)
	print('error = ', a05 - a2)


def searchRange(A, B):
	'''
	Binary search for start and end of range filled with int B
	
	1. Binary search for B
	2. Binary search for first B from low non-B to found B
		found when test pos looks like:
		...t, B... or ...n, Bt...
	3. Binary search for last B from found B to high non-B
		found when test pos looks like:
		...tB, n... or ...B, t...
	
	Handle 0 = B and last = B
	'''
	
	start, end, firstFound, results = 0, len(A) -1, -1, [-1,-1]
	if A[0] == B:
		results[0] = 0
	if A[-1] == B:
		results[1] = len(A)-1
		
	if results[0]>=0 and results[1]>=0:
		return results
		
	while start <= end:
		test = (start + end)//2
		# print("Finding first: s:{} e:{} t:{}".format(start,end,test))
		if A[test] == B:
			firstFound = test
			break
		elif A[test] < B:
			start = test + 1
		elif A[test] > B:
			end = test - 1
	
	if firstFound == -1:
		return results

	results = [firstFound, firstFound]
	
	temp = end

	end = firstFound
	while start < end:
		test = (start + end)//2
		# print("Finding start: s:{} e:{} t:{}".format(start,end,test))
		if A[test] == B:
			end = test
		else:
			start = test + 1
			
	results[0] = start if A[start] == B else end
	
	start, end = firstFound, temp
	while start < end - 1:
		test = (start + end)//2
		# print("Finding end: s:{} e:{} t:{}".format(start,end,test))
		if A[test] == B:
			start = test
		else:
			end = test - 1
	
	results[1] = end if A[end] == B else start
	
	return results

A = [
		[1,2,3,4,5,6,7,8,8,8,8,8,8,8,8,8,8,8,9,10,11,12,13,14,15],
		8,
		[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ],
		10,
		[ 1, 2, 6, 9, 9 ],
		2,
		[1],
		1,
		[1,2,3,4,5,6,7],
		8,
	]


for i in range(0, len(A), 2):
	print('Finding {} in A'.format(A[i+1]) )
	print( searchRange(A[i],A[i+1]))


def findMinRot(A):
	'''
	Find minimum in a rotated array
	i.e. [4,5,6,7,0,1,2,3]
	'''
	start, end = 0, len(A)-1
	while start <= end:
		if A[start] < A[end]:
			return start
		test = (end + start)//2
		print("s:{} e:{} t:{} ".format(start,end,test))
		if A[test] < A[(test+1)%len(A)] and A[test] < A[(test-1)%len(A)]:
			return test
		elif A[start] <= A[test]:
			start = test + 1
		elif A[end] >= A[test]:
			end = test - 1
	return -1

A = [
		[4,5,6,7,0,1,2,3],
		[1,2,3,4,5,6,7,8],
		[8,1,2,3,4,5,6,7],
		[2,3,4,5,6,7,8,1],
		[ 40342, 40766, 41307, 42639, 42777, 46079, 47038, 47923, 48064, 48083, 49760, 49871, 51000, 51035, 53186, 53499, 53895, 59118, 60467, 60498, 60764, 65158, 65838, 65885, 65919, 66638, 66807, 66989, 67114, 68119, 68146, 68584, 69494, 70914, 72312, 72432, 74536, 77038, 77720, 78590, 78769, 78894, 80169, 81717, 81760, 82124, 82583, 82620, 82877, 83131, 84932, 85050, 85358, 89896, 90991, 91348, 91376, 92786, 93626, 93688, 94972, 95064, 96240, 96308, 96755, 97197, 97243, 98049, 98407, 98998, 99785, 350, 2563, 3075, 3161, 3519, 4176, 4371, 5885, 6054, 6495, 7218, 7734, 9235, 11899, 13070, 14002, 16258, 16309, 16461, 17338, 19141, 19526, 21256, 21507, 21945, 22753, 25029, 25524, 27311, 27609, 28217, 30854, 32721, 33184, 34190, 35040, 35753, 36144, 37342 ],

	]

for i in A:
	print( findMinRot(i))



def powMod(self, x, n, d):
	if n==0:
		return 1 % d
	
	memo = {}
	def _k(*p):
		return '+'.join([ str(i) for i in p ])
		
	''' 
	for even exp
	x^n == (x * x)^n/2
	'''
	def recurse(base, exp, memo):
		if exp == 0:
			return 1
			
		k = _k(base, exp)
		if k in memo:
			return memo[k]
		
		res = 0
		if exp % 2 == 0:
			res = recurse((base * base), exp/2, memo)
		else:
			res = base * recurse((base * base), (exp - 1)/2, memo)
			
		memo[k] = res
		return res
	
	return recurse(x, n, memo) % d


def pow(x, n):
	if n==0:
		return 1
	
	memo = {}
	def _k(*p):
		# return '+'.join([ str(i) for i in p ])
		return p
		
	''' 
	for even exp
	x^n == (x * x)^n/2
	'''
	def recurse(base, exp, memo):
		if exp == 0:
			return 1

		if exp == 1:
			return base
			
		k = _k(base, exp)
		if k in memo:
			# print("memo hit {}**{}".format(base, exp))
			return memo[k]

		'''
		10**10

		(((10 * 10) * (10 * 10)) * ((10 * 10) * (10 * 10))) * (10 * 10)

		'''
		# if base in memo:
		# 	print("memo hit {}".format(base))
		# 	mult = memo[base]  
		# else: 
		# 	mult = base * base
		# 	memo[base] = mult
		
		res = 0
		if exp % 2 == 0:
			res = recurse(base, exp//2, memo) * recurse(base, exp//2, memo)
		else:
			res = base * recurse(base, (exp - 1)//2, memo) * recurse(base, (exp - 1)//2, memo)
			
		memo[k] = res
		return res
	
	return recurse(x, n, memo)

A = [ 
	(2,4),
	(202, 8),
	(10, 5),
	(1001, 207),
	# (402141,21311),
	# (71045970,41535484), #DOESN'T FINISH
]

for a in A:
	print("pow result = {}".format(pow(*a)))
	print("** result = {}".format(a[0]**a[1]))


def binSearchRotatedForArray(A, B):
	'''
	rotated cases (looking for pivot):
	start < end = already sorted
	mid-1 > mid < mid+1 = pivot
	start < mid = pivot in mid - end
	mid < end = pivot in start - mid
	
	extend to looking for X:
	Step 1 find pivot.
	Step 2 perform binary search with range % pivot....
	....might work
	'''
	def findPivot(A):
		if len(A) == 1:
			return 0

		start = 0
		end = len(A)-1
		
		while start <= end:
			if A[start] < A[end]:
				return start
			mid = (start + end)//2
			print("s:{} e:{} m:{} A[m]:{}".format(start, end, mid, A[mid]))
			if A[mid] < A[(mid-1)%len(A)] and A[mid] < A[(mid+1)%len(A)]:
				return mid
			if A[start] <= A[mid]:
				start = mid + 1
			elif A[end] >= A[mid]:
				end = mid - 1
	
	pivot = findPivot(A)
	print('Pivot found is {}'.format(pivot))
	
	start = 0
	end = len(A)-1
	while start <= end:
		mid = (start + end)//2
		test = A[(mid + pivot) % len(A)] if pivot > 0 else A[mid]
		print("s:{} e:{} m:{} A[midMod]:{} B:{} piv:{} midPlusPivModPiv:{}".format(start, end, mid, A[(mid + pivot) % len(A)], B, pivot, (mid + pivot) % len(A)))
		if test == B:
			return (mid + pivot) % len(A) if pivot > 0 else mid
		elif test < B:
			start = mid + 1
		elif test > B:
			end = mid - 1
			
	return -1

A = [ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ]
B = 202

print(binSearchRotatedForArray(A,B))

A = [ 9, 10, 12, 13, 24, 26, 27, 28, 29, 43, 48, 51, 54, 56, 57, 59, 62, 66, 70, 71, 72, 74, 75, 77, 78, 81, 83, 85, 87, 88, 89, 90, 91, 92, 93, 97, 98, 99, 101, 102, 104, 105, 107, 112, 113, 115, 123, 126, 127, 132, 133, 134, 135, 136, 143, 144, 148, 150, 151, 152, 154, 159, 160, 161, 163, 167, 169, 170, 174, 176, 177, 179, 180, 181, 183, 185, 186, 187, 188, 193, 194, 196, 197, 198, 199, 200, 203, 1, 6, 7, 8 ]
B = 38

print(binSearchRotatedForArray(A,B))

A = [ 192, 194, 197, 198, 199, 200, 201, 203, 204, 2, 3, 4, 7, 9, 10, 11, 14, 15, 16, 17, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 33, 34, 35, 36, 39, 40, 42, 43, 46, 47, 50, 51, 52, 53, 55, 57, 59, 60, 64, 66, 68, 70, 71, 72, 75, 76, 78, 85, 86, 87, 91, 92, 94, 95, 96, 99, 102, 105, 106, 107, 109, 111, 113, 114, 115, 119, 120, 121, 123, 125, 129, 130, 131, 133, 134, 137, 138, 139, 140, 141, 142, 143, 145, 146, 149, 151, 152, 156, 160, 161, 165, 167, 168, 170, 171, 176, 177, 178, 179, 180, 181, 182, 185, 186, 190 ]
B = 70

print(binSearchRotatedForArray(A,B))




def findCount( A, B):
	'''
	Binary search to find the element.
	Binary search to find the start of element
	Binary search to find the end of element
	
	subtract end - start = # of occurences
	'''
	start = 0
	end = len(A)-1
	first = -1
	while start < end:
		mid = (start + end)//2
		print("s:{} e:{} mid:{} A[mid]:{} B:{}".format(start, end, mid, A[mid], B))
		if A[mid] == B:
			first = mid
			break
		elif A[mid] < B:
			start = mid + 1
		elif A[mid] > B:
			end = mid -1
	if first == -1:
		return 0 #No occurences
		
	#Find the lower B
	start = 0
	end = first - 1
	lower = -1
	while start <= end:
		mid = (start + end)//2
		print("lower s:{} e:{} mid:{} A[mid]:{} B:{}".format(start, end, mid, A[mid], B))
		if A[start] != B and A[end] != B:
			lower = end + 1
			break
		elif mid == 0:
			lower = mid
			break
		elif A[mid] == B and A[mid - 1] != B:
			lower = mid
			break
		elif A[mid] == B:
			end = mid-1
		elif A[mid] != B:
			start = mid + 1
		
	
	#Find the upper B
	start = first + 1
	end = len(A) - 1
	upper = -1
	while start <= end:
		mid = (start + end)//2
		print("upper s:{} e:{} mid:{} A[mid]:{} B:{}".format(start, end, mid, A[mid], B))
		if A[start] != B and A[end] != B:
			upper = start - 1
			break
		elif mid == len(A) - 1:
			upper = mid
			break
		elif A[mid] == B and A[mid + 1] != B:
			upper = mid
			break
		elif A[mid] == B:
			start = mid+1
		elif A[mid] != B:
			end = mid - 1
	print(upper, lower)
	return upper - lower + 1


# A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]

A = [1,2,2,2,2,3,4,5]
B = 2



print(findCount(A,B))


def zigzag(A, B):
	if B == 1:
		return A
	row = 0
	direction = 1
	rows = []
	i = 0
	while True:
		if len(rows) - 1 < row:
			rows.append([])
		rows[row].append(A[i])
		direction *= -1 if row+direction < 0 or row+direction == B else 1
		row = row + direction
		print("row:{} direction:{} rows:{}".format(row, direction, rows))
		i += 1
		if i == len(A):
			break
	
	out = ''.join([ ''.join(r) for r in rows if r != None ])
	return out

A = "ROGERISWINNING"
B = 3

# A = "kHAlbLzY8Dr4zR0eeLwvoRFg9r23Y3hEujEqdio0ctLh4jZ1izwLh70R7SAkFsXlZ8UlghCL95yezo5hBxQJ1Td6qFb3jpFrMj8pdvP6M6k7IaXkq21XhpmGNwl7tBe86eZasMW2BGhnqF6gPb1YjCTexgCurS"
# B = 1

print(zigzag(A,B))


def atoi(A):
	sign = 1
	a = A.strip()
	nums = list("0123456789")
	sumNum = 0
	for c in a:
		if c in ['+', '-'] and sumNum == 0:
			sign = -1 if c == '-' else 1
			continue
		if not c in nums and sumNum == 0:
			return 0
		if not c in nums:
			break
		if c in nums:
			sumNum *= 10
			sumNum += nums.index(c)

	sumNum *= sign
	
	if sumNum > 2147483647:
		sumNum = 2147483647
	elif sumNum < -2147483648:
		sumNum = -2147483648
			
	return sumNum

A = "-88297 248252140B12 37239U4622733246I218 9 1303 44 A83793H3G2 1674443R591 4368 7 97"

print(atoi(A))


def strMultiply( A, B):
	if A=='0' or B=='0':
		return '0'
	nums = list('0123456789')
	a = A[::-1] #reverse
	b = B[::-1] #reverse
	#convert to list of digits
	a = [nums.index(d) for d in a]
	b = [nums.index(d) for d in b]
	# print("a:{} b:{}".format(a, b))
	
	carry = 0
	digits = []
	'''
	202
	 91
	___
	  1 x 202 = 202
	+ 90 x 202 = 10 * (9 * 2 = 8 c 1, 9 * 0 + 1c = 1, 9 * 2 + 0c = 8 c 1, 9 * 0 + 1c = 1)


	99999
	99999
	_____

	9 x 9 = 1 c8, 9 x 9 + 8 = 9 c8, 9 x 9 + 8 = 9 c8, 9 x 9 + 8 = 9 c8, 9 x 9 + 8 = 9 c8, 0 x 9 + 8 = 8
	> 9 x 9 = 1 c8 + 9 = 0 c9, 9 x 9 + 8 = 9 c8, 9 x 9 + 8 = 9 c8, 9 x 9 + 8 = 9 c8, 9 x 9 + 8 = 9 c8, 0 x 9 + 8 = 8

	1, 9, 9, 9, 9, 8
	0, , 
	'''
	i = 0
	for da in a:
		j = i
		for db in b:
			if len(digits) -1 < j:
				digits.append(0)
			digits[j] += da * db + carry
			carry = digits[j]//10
			digits[j] %= 10
			# print(digits, carry, i, j)
			j += 1
		if carry > 0:
			if len(digits) - 1 < j:
				digits.append(0)
			digits[j] += carry
			carry = 0
		i += 1
	
	while True:
		if digits[-1] != 0:
			break
		digits.pop()

	return ''.join([ str(n) for n in digits[::-1]])


A = "99999"
B = "99999"

print(strMultiply(A,B))


A = "202"
B = "91"

print(strMultiply(A,B))

A = "202927392794610473036503629403628295826"
B = "0092972662936629465926527496251141"

print(strMultiply(A,B))
print("A * B", int(A) * int(B))

