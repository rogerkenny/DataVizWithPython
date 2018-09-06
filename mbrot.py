'''
GOAL:
Understand decorators and generators in Python by creating ASCII Mandelbrot set

Z1 -> Z * Z + C
'''

def mandelbrotGenerator(C, i):
	Z = 0+0j
	j = 0
	while j < i:
		Z = (Z * Z) + C
		yield Z
		j += 1

def generate(output=None):
	width, height = 93, 33

	realMin, realMax = -2.0+0j, 1.0+0j
	imagMin, imagMax = 0-1.0j, 0+1.0j

	palette = "*=:-."
	fill = " "

	iterations = 100

	if output == None:
		output = ''

	dw = (realMax - realMin)/width
	dh = (imagMax - imagMin)/height
	
	for h in range(height):
		for w in range(width):
			C = (realMin + (w * dw)) + (imagMin + (h * dh))
			i = 0
			for z in mandelbrotGenerator(C, iterations):
				if abs(z) >= 20:
					output += palette[i%len(palette)]
					break
				i += 1
			else:
				# Stayed small. Mark as part of the set
				output += fill
		output += "\n"

	print(output)


generate()

