# coding: utf-8
import random
import json

def _k(path):
	return '+'.join(path)

def chooseNext(paths, path):
	# print("chooseNext", path)
	pkey = _k(path)
	# print("_k", pkey)
	if not pkey in paths:
		return None
	nodes = []
	weights = []
	for n, w in paths[pkey].items():
		nodes.append(n)
		weights.append(w)
	return random.choices(nodes, weights)[0]
	

def generate(paths, maxChars=140, seed='', pathLen=1, temp=1):
	count = len(seed)
	out = seed.split(' ')
	s = seed.split(' ')
	next = ''
	while True:
		#print("generate", out, s)
		a = 1 if random.random() <= temp else 0
		v = a * random.randint(0,len(s)-1)
		#print(v, s[v:])
		next = chooseNext(paths, s[v:])
		if next == None:
			if len(s) > 1:
				s.pop(0)
				continue
			out.pop()
			s=['']
			continue
		if count + len(next) + 1 > maxChars:
			break
		out.append(next)
		s = out[(-1 * pathLen):]
		count += len(next) + 1 
		#account for space with 1
	out = (' '.join(out)).lstrip()
	#try to end with a real line by 
	#stripping last line without \n
	if out[:-1] != '\n':
		out = out.splitlines()
		if len(out) > 1:
			out.pop()
		out = '\n'.join(out)
	return out
	

def makegrunge(request):
	if 'seed' in request.args:
		seed = request.args['seed']
	else:
		seed = ''

	if 'chars' in request.args:
		ch = int(request.args['chars'])
	else:
		ch = maxChars

	if 'temp' in request.args:
		t = float(request.args['temp'])
	else:
		t = 0.52

	out = ''
	out += generate(p, maxChars=ch, pathLen=pLen, seed=seed, temp=t)
	return (out, {"Content-Type": "text/plain; charset=utf-8"})
	
pLen = 3
dumpFile = 'PDump.json'
maxChars = 280

inFile = open(dumpFile, 'r')
p = json.load(inFile)
inFile.close()
