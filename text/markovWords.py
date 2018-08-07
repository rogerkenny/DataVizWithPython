# coding: utf-8
import string
import random
import glob
import json
import tweepy

def _k(path):
	return '+'.join(path)		

def makeChain(fileName, pathLen=1, paths={}):
	fin = open(fileName, 'r')
	 
	foundWord = ''
	foundWords = ['']
	
	replacements = { 
		"i'm" : "I'm",
		'i' : 'I',
		"i'll" : "I'll",
		'oz' : '40oz',
		
	}
	
	while True:
		ch = fin.read(1)
		if not ch:
			break
		if ch.isalpha() or ch in ["'", ".", "?", "!", "\n", "-"]:
			foundWord += ch
		else:
			if len(foundWord) > 0:
				if len(foundWord) == 1 and foundWord not in ['a','i', 'I']:
					foundWord = ''
					continue
				if foundWord in replacements:
					foundWord = replacements[foundWord]
				fw = foundWords[0:]
				while len(fw) > 0:
					pathKey = _k(fw)
					if pathKey not in paths:
						paths[pathKey] = {foundWord : 1}
					else:
						if foundWord in paths[pathKey]:
							paths[pathKey][foundWord] += 1
						else:
							paths[pathKey][foundWord] = 1
					fw.pop(0)
				foundWords.append(foundWord)
				if len(foundWords) > pathLen:
					foundWords.pop(0)
				foundWord = ''
	fin.close()
	return paths

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

def writeChain(p, fileName):
	out = open(fileName, 'w')
	json.dump(p, out)
	out.close()
	
	
pLen = 3
p = {}
dumpFile = 'PDump.json'

def regenerateChain():
	lyricFiles = glob.glob("lyrics/*.txt")
	paths = {}

	for l in lyricFiles:
		p = makeChain(l, pathLen=pLen, paths=paths)
		
	writeChain(p, dumpFile)
	return p
	

'''Twitter api'''	
api = None
def twitterConnect():
	creds = open("CRED.txt", "r")
	
	consumer_key, consumer_secret = creds.readline().strip(), creds.readline().strip()
	access_token, access_token_secret = creds.readline().strip(), creds.readline().strip()
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	return tweepy.API(auth)

def tweet(t):
	api = twitterConnect()

	print('Tweeting ...')
	#print(api.me())
	tw = api.update_status(t)
	print(t)

def findTweets(f):
	api = twitterConnect()
	print('Finding ...', f)
	s = tweepy.Cursor( api.search, q=f)
	#nav tweets interface
	for t in s.items():
		#print(t.screen_name)
		print(t.id)
		print(t.text)
		#print(t.url)
		
		print('-'*40)
		n = input('>>')
		if n == 'r':
			print('REPLY TO ', t.id)
		elif n == 'i':
			print(t)
		elif n == 'u':
			print(t.user.screen_name)
			print(t.user.location)
			print(t.user.url)
			print(t.user)
		elif n == 'q':
			return 
		else:
			continue
		

'''True to regenerate chain json'''
if True:
	p = regenerateChain()
else:
	inFile = open(dumpFile, 'r')
	p = json.load(inFile)
	inFile.close()

maxChars = 140*2
# print(p)
print('='*40)
gen = generate(p, pathLen=pLen, seed='', maxChars=maxChars, temp=0.5)
print(gen)


s = ''
while True:
	print('='*40)
	s = input('% ')
	if s == 'exit':
		break
	if s == 't':
		tweet(gen)
		continue
	if s == 'f':
		q = input('find>')
		if q == 'c':
			continue
		findTweets(q)
		continue	
	gen = generate(p, pathLen=pLen, seed=s, maxChars=maxChars, temp=0.55)
	print(gen)
	
