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

def algorithm(generator, width, height, rule, iterations, dw, dh, center, palette, fill):
	wOffset, hOffset = width//-2, height//-2
	output = ''
	for h in range(height):
		for w in range(width):
			C = (((w + wOffset) * dw) + ((h + hOffset) * dh)) + center
			i = 0
			for z in generator(C, iterations, rule):
				if abs(z) >= 20:
					output += palette[i%len(palette)]
					break
				i += 1
			else:
				# Stayed small. Mark as part of the set
				output += fill
		output += "\n"

	return output


def generate(f):
	
	def decoratedAlgorithm():
		generator=mandelbrotGenerator

		width, height = 93, 33

		realMin, realMax = -2.0+0j, 1.0+0j
		imagMin, imagMax = 0-1.0j, 0+1.0j

		# Colors http://web.archive.org/web/20131009193526/http://bitmote.com/index.php?post/2012/11/19/Using-ANSI-Color-Codes-to-Colorize-Your-Bash-Prompt-on-Linux

		colors = [196+24, 196+12, 160 +9, 124+1, 16+5]

		palette = "*=:-." if not color else [ '\033[48;5;{}m \033[m'.format(x) for x in colors ]
		fill = "█" if not color else '\033[48;5;0m \033[m'

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

		# useRule
		try:
			print(f(generator, width, height, rules[useRule], iterations, dw, dh, center, palette, fill))
		except:
			for r in rules:
				print(f(generator, width, height, r, iterations, dw, dh, center, palette, fill))

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
