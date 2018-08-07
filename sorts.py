s = [
	[1,50,3,6,77,55,2,20,22,7,8,51,102,4],
	[2,3,6,7,8,44,55,66,77,88,99,100],
	[7, 19, 37, 61, 127, 271, 331, 397, 547, 631, 919, 1657, 1801, 1951, 2269, 2437, 2791, 3169, 3571, 4219, 4447, 5167, 5419, 6211, 7057, 7351, 8269, 9241, 10267, 11719, 12097, 13267, 13669, 16651, 19441, 19927, 22447, 23497, 24571, 25117, 26227, 27361, 33391, 35317,13, 109, 193, 433, 769, 1201, 1453, 2029, 3469, 3889, 4801, 10093, 12289, 13873, 18253, 20173, 21169, 22189, 28813, 37633, 43201, 47629, 60493, 63949, 65713, 69313, 73009, 76801, 84673, 106033, 108301, 112909, 115249, 2, 5, 11, 101, 181, 1181, 1811, 18181, 108881, 110881, 118081, 120121, 121021, 121151, 150151, 151051, 151121, 180181, 180811, 181081]
	]

'''When counting possibilities, iterate on decisions, not value'''


# coding: utf-8
def bubble(l):
	lastPlace = 0
	while lastPlace < len(l):
		for i in range(0, len(l) - lastPlace - 1):
			if l[i] > l[i+1]:
				temp = l[i]
				l[i] = l[i+1]
				l[i+1] = temp
		lastPlace += 1
		
def merge(l):
	'''Merge sort'''
	t=[None]*len(l)
	_merge(l,0,len(l)-1,t)
	
def _merge(l, leftStart, rightEnd, temp=[]):
	if leftStart >= rightEnd:
		return 
	# middle = leftStart + rightEnd // 2 
	middle = (rightEnd - leftStart) // 2 + leftStart

	# print(leftStart, middle, middle + 1, rightEnd)

	_merge(l, leftStart, middle, temp)
	_merge(l, middle + 1, rightEnd, temp)
	
	_mergeLR(l, leftStart, middle, middle + 1, rightEnd, temp)
	return
	
def _mergeLR(l, leftStart, leftEnd, rightStart, rightEnd, temp=[]):
	#TODO
	i = 0
	li = leftStart
	ri = rightStart
	lenl = len(l)
	while li <= leftEnd and ri <= rightEnd:
		if l[li] <= l[ri]:
			temp[i] = l[li]
			li +=1
		else:
			temp[i] = l[ri]
			ri +=1
		i += 1
	
	#copy remaining left and right into temp
	for e in l[li:leftEnd + 1]:
		temp[i] = e
		i+= 1
	for e in l[ri:rightEnd + 1]:
		temp[i] = e
		i+=1
		
	#copy temp back to l
	l[leftStart:rightEnd + 1] = temp[0:(rightEnd-leftStart) + 1]
	
		
	

for l in s:
	extra = l
	bubble(extra)
	print ('Bubble', extra)
	extra = l
	merge(extra)
	print ('Merge', extra)
