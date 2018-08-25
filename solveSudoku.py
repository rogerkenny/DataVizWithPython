import sys, time
from random import shuffle

def solveSudoku(A):
	a = [ list(r) for r in A ]
	#print(a)
	mysteryCells = []
	for ri in range(len(A)):
			for ci in range(len(A[ri])):
				if A[ri][ci] == '.':
					mysteryCells.append((ri, ci))

	mobile = False
	# start = True

	def drawFrame(S):
		if not mobile:
			# if not start:
			sys.stdout.write(u"\u001b[1000D") # Move left
			sys.stdout.write(u"\u001b[" + str((len(S))) + "A") #move up
			# start = False
			print('\n'.join([''.join(r) for r in S]))
			# time.sleep(0.01)
	
	def solve(a, mysteryCells, cellI, A):
		'''
		cell is going to be [row, col]
		'''
		'''
		if No unset cells return A
		'''
		if len(mysteryCells) == cellI:
			A = [''.join(r) for r in a]
			# print('\n'.join([''.join(r) for r in a]))
			return True
		
		mya = [r[:] for r in a]
		
		cell = mysteryCells[cellI]
			
		rowSet = {'1','2','3','4','5','6','7','8','9'}
		colSet = {'1','2','3','4','5','6','7','8','9'}

		for row in mya:
			if row[cell[1]] != '.':
				rowSet.remove(row[cell[1]])
		
		for col in mya[cell[0]]:
			if col != '.':
				colSet.remove(col)
		
		#print(rowSet, colSet)
		
		possibleVals = rowSet & colSet
		if len(possibleVals) == 0:
			return False
		
		for v in possibleVals:
			mya[cell[0]][cell[1]] = v
			drawFrame(mya)
			result = solve(mya, mysteryCells, cellI + 1, A)
			
			if result:
				return result
	
	solve(a, mysteryCells, 0, A)
	


A = [ "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ]

# print(A)
solveSudoku(A)
print(A)
