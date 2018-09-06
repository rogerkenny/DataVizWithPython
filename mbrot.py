'''
GOAL:
Understand decorators and generators in Python by creating ASCII Mandelbrot set

Z1 -> Z * Z + C
'''
from functools import wraps

def mandelbrotGenerator(C, i, rule):
	Z = 0+0j
	j = 0
	while j < i:
		Z = rule(Z, C)
		yield Z
		j += 1

def algorithm(generator, width, height, rule, iterations, dw, dh, center):
	wOffset, hOffset = width//-2, height//-2
	output = []
	for h in range(height):
		row = []
		for w in range(width):
			C = (((w + wOffset) * dw) + ((h + hOffset) * dh)) + center
			i = 0
			for z in generator(C, iterations, rule):
				if abs(z) >= 20:
					row.append(i)
					break
				i += 1
			else:
				# Stayed small. Mark as part of the set
				row.append(-1)
		output.append(row)

	return output

def colorStringFromList(l):
	# Colors http://web.archive.org/web/20131009193526/http://bitmote.com/index.php?post/2012/11/19/Using-ANSI-Color-Codes-to-Colorize-Your-Bash-Prompt-on-Linux
	colors = [196+24, 196+12, 160 +9, 124+1, 16+5]
	def c(x):
		if x < 0:
			return '\033[48;5;0m'
		else:
			return '\033[48;5;{}m'.format(colors[x%len(colors)]) 

	out = []
	lastNum = None
	for n in l:
		if n != lastNum:
			if len(out) != 0:
				#terminate last color
				out.append('\033[m')
			out += c(n)
			lastNum = n
		out.append(' ')
	out.append('\033[m')
	return ''.join(out)

def asciiStringFromList(l):
	palette = "*=:-."
	def a(x):
		if x < 0:
			return "█"
		else:
			return palette[x%len(palette)]
	out = []
	for n in l:
		out.append(a(n))
	return ''.join(out)


def generate(f):
	
	def decoratedAlgorithm():
		generator=mandelbrotGenerator

		width, height = 93, 33

		realMin, realMax = -2.0+0j, 1.0+0j
		imagMin, imagMax = 0-1.0j, 0+1.0j

		iterations = 100

		try:
			iterations *= iFactor
		except:
			pass

		dw = (realMax - realMin)/width
		dh = (imagMax - imagMin)/height

		try:
			dw /= zoom
			dh /= zoom
		except:
			pass

		rules = [
			lambda z, c: z**1.125 + c,
			lambda z, c: z**1.25 + c,
			lambda z, c: z**1.5 + c,
			lambda z, c: z**1.9 + c,
			lambda z, c: z**2 + c,
			lambda z, c: z**2.2 + c,
			lambda z, c: z**3 + c,
			lambda z, c: z**4 + c,
			lambda z, c: z**5 + c,
			lambda z, c: z**6 + c,
		]

		#zoomcenter
		try:
			center = zoomcenter
		except Exception as e:
			center = -0.50+0.0j

		renderer = colorStringFromList if color else asciiStringFromList

		# useRule
		try:
			print('\n'.join( list(map( renderer, f(generator, width, height, rules[useRule], iterations, dw, dh, center)))))
			print("\n")
		except:
			for r in rules:
				print('\n'.join( list(map( renderer, f(generator, width, height, r, iterations, dw, dh, center)))))
				print("\n")


	return decoratedAlgorithm


makeMandelbrot = generate(algorithm)
color = False

makeMandelbrot()

color = True

makeMandelbrot()

zoomcenter = -0.70176-0.3842j
useRule = 4

zoom = 10
iFactor = 2
makeMandelbrot()

zoomcenter = -0.8+0.156j
zoom = 1000
iFactor = 3
makeMandelbrot()
color = False
makeMandelbrot()

zoomcenter = -0.7269+0.1889j
makeMandelbrot()
color = True
makeMandelbrot()

zoom = 10
zoomcenter = -0.4+0.6j
makeMandelbrot()

zoomcenter = -0.8j
makeMandelbrot()

zoomcenter = -1.8
makeMandelbrot()
color = False
makeMandelbrot()


