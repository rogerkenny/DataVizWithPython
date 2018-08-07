# coding: utf-8
import glob
#import urllib2
import requests
import re
from bs4 import BeautifulSoup

files = glob.glob('linksToLyrics/Nirvana*.txt')

print('$'*40)
#print(files)

'''Parse list of song links'''
file = open(files[0], 'r')
songLinks = []
bandTitle = file.readline()
numOfAlbums = int(file.readline().strip())
for ai in range(numOfAlbums):
	albumTitle = file.readline()
	numOfSongs = int(file.readline().strip())
	for si in range(numOfSongs):
		songLinks.append(file.readline().strip())
		
file.close()

#print(songLinks)
#pageurl = 'http' + songLinks[0][5:]

pageurl = songLinks[4]
print(pageurl)

#page = urllib2.urlopen(pageurl)

res = requests.get(pageurl)
page = res.text
#fin = open('songEx.txt', 'r')
#page = fin.read()
soup = BeautifulSoup(page, 'html.parser')

title = soup.title.text.strip()
print(title)
#print(soup.prettify())

'''cache while in dev'''
#out = open('songEx.txt', 'w')
#out.write(soup.prettify())
#out.close()

ring = soup.find('div', 'ringtone')
text = ring.findNext('div').text
text = '\n'.join([ l.strip() for l in text.split('\n')])
#text = re.sub(' +', ' ',  text)
text = re.sub('\n\n+', '\n', text)
#text = text.strip()
#text = re.sub(' +', ' ', text)

print(text)

fileName = title + '|' + (re.sub('[/:]', '-', pageurl)) + '.txt'
fout = open('lyrics/' + fileName , 'w')
fout.write(text)
fout.close()


		

