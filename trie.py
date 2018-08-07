#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

class Trie:
    def __init__(self):
        '''Dict of dicts'''
        self.root = {"leaves" : 0}
        self.sentinel = '#'
        
    def __repr__(self):
        o = ''
        max = 10
        q = [self.root]
        self.root['depth'] = 0
        depth = 0
        while depth < max and len(q) > 0:
            c = q.pop()
            if "depth" in c and c["depth"] == depth:
                depth += 1
                o += "\n"
            for k, n in c.items():
                if k != self.sentinel and k != 'depth' and k != 'leaves':
                    o += k 
                    q.append(n)
                    n["depth"] = depth
            o += " "
        return o
        
    def add(self, word):
        path = self.find(word, self.root)
        if path[-1] == None: #partial word found. Start at len(path) - 1
            path.pop(-1) 
            #Remove last element which is None
            insertPoint = path[-1] 
            #get last node if partial string found (same prefix) 
            #else start insert at the root
            #
            #  word = "word"
            # 
            #           insertPoint ↓
            #  path = [{$},{w},{o},{r}]
            #
            #   or
            #        insertPoint ↓
            #           path = [{$}]  
            #
            s = len(path)-1
            for ch in word[s:]:
                insertPoint[ch] = {}
                insertPoint = insertPoint[ch]
                path.append(insertPoint)
        else: #whole word found
            insertPoint = path[-1]
            if self.sentinel in insertPoint:
                #already marked as a word
                return
        insertPoint[self.sentinel] = 1 #mark word
        for n in path:
            if n == None: #should never happen
                continue
            if "leaves" in n:
                n['leaves'] += 1
            else:
                n['leaves'] = 1        

    def find(self, pre, node):
        '''Returns path starting with node. Ends with None if pre is not completly found'''
        found = [node]
        search = node
        for c in pre:
            if c in search:
                found.append(search[c])
            else:
                found.append(None)
                break
            search = search[c]
        return found
    
    def count(self, pre):
        found = self.find(pre, self.root)
        if len(found) == 0 or found[-1] == None:
            return 0
        return found[-1]['leaves']  
       
def processLine(opContact):
    opContact = opContact.split()
    op = opContact[0]

    contact = opContact[1]
    if op == 'add':
        t.add(contact)
        # print(contact)
    elif op == 'find':
        print(t.count(contact)) 
        

if __name__ == '__main__':
    t = Trie()

    f = open('contact_001.txt', 'r')
    
    n = int(f.readline())

    for n_itr in range(n):
        opContact = f.readline()

        processLine(opContact)

    while True:
        nOpCont = input()
        if nOpCont == 'end':
            break
        processLine(nOpCont)
        



