# coding: utf-8
import urllib2
import re
from bs4 import BeautifulSoup



tllfile = open('topLevelLinks.txt', 'r')

tll = tllfile.readlines()
tll = [t.strip() for t in tll]
#print(tll)

tllfile.close()

#t = tll[0]

def getLyricLinks(t):
	tld = t[:24]
	
	page = urllib2.urlopen(t)
	#pagef = open('ex.txt', 'r')
	#page = pagef.read()
	soup = BeautifulSoup(page, 'html.parser')
	
	title = soup.title
	print(title.text.strip())
	#out = open('ex.txt', 'w')
	#out.write(soup.prettify())
	#out.close()
	
	albums = soup.find(id='listAlbum')
	
	divs = soup.find_all('div')
	for d in divs:
		d.name = 'a'
	
	#Only want songs from the 90s
	child = albums.findChild('a')	
	nintiesLinks = {}
	lastAlbum = ''
	nFile = open(title.text.strip() + '.txt', 'w')
	
	while True:
		if child == None:
			break
		c = child.get('class')
		if c != None and 'album' in c:
			#print("CLASS = ", child['class'])
			t = (child.getText()).strip()
			t = re.sub(' +', ' ', t)
			t = re.sub('\n', '', t)
			print (t)
			#see if text in div ends in 9.. 
			#only true for 90s albums
			if len(t) < 3 or t[-3] != '9':
				child = child.findNext('a','album')
				continue
			lastAlbum = t
			nintiesLinks[t] = []
			child = child.findNext('a')
			continue
		else:
			if 'href' not in child.attrs:
				child = child.findNext('a')
				continue
			else:
				link = '{2}{0}'.format(child['href'][2:], (child.getText()).strip(), tld)
				nintiesLinks[lastAlbum].append(link)
				#print(link)
		child = child.findNext('a')
	
	nFile.write(title.text.strip())
	nFile.write('\n')
	nFile.write(str(len(nintiesLinks.keys())))
	nFile.write('\n')
	for a, songs in nintiesLinks.items():
		nFile.write(a)
		nFile.write('\n')
		nFile.write(str(len(songs)))
		nFile.write('\n')
		for s in songs:
			nFile.write(s)
			nFile.write('\n')
	nFile.close()
	
	
for t in tll:
	getLyricLinks(t)
