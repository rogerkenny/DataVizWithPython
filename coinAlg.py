#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

'''

12
[2,4,5]




2 + [10]
2,2,2,2,2,2
4 + [8]
4,2,2,2,2
5 + [7] -> 
    2 + [5] ->
        2 + [3] ->
            2 + [1] ->
             1 + [-1] = None
        
5,2,2,2X

1
1 2 3

1
w = []
for 1 2 3
    dw = gs( 1 - 1, 123, ) -> [[]] (due to zero)
    for d in [[]]
        d = [1]
        w = [[1]]
return [[1]]

2
w = []
for 1 2 3
    dw = gs( 2 - 1, 123) -> [[1]]
    for d in [[1]]
        d = [1,1]
        w = [[1,1]]
    dw = gs( 2 - 2, 123) -> [[]] 
    for d in [[]]
        d = [2]
        w = [[1,1], [2]]
return [[1,1], [2]]

3
for 123
    dw = gs( 3 - 1, 123) -> [[1,1], [2]]
    for d in [[1,1], [2]]
        d = [1,1,1]
        w = [[1,1,1]]
        d = [2, 1]
        w = [[1,1,1], [2,1]]
    dw = gs( 3 - 2 ) -> [[1]]
    for d in [[1]]
        d = [1, 2]
        w = [[1,1,1], [2,1], [1,2]]


Recursive Tree

12
[2,4,5]


                                                                         [12]
            2 + [10]                                                     4 + [8]                          5 + [7]
2 + [8]         4 + [6]               5 + [5]                    2 + [6] 4 + [4] 5 + [3]         2 + [5]  4 + [3]  5 + [2] 
memo     2 + [4] 4 + [2] 5 + [1]      2 + [3] 4 +[1] 5 + [0]

ALL WRONG! I WAS ITERATING OVER VALUE AND NOT POSSIBILITES!

'''
minCoin = -1

# Complete the ways function below.
def ways(n, coins):
    memo = {}
    minCoin = min(coins)
    ways = getSets(n, coins, memo)
    # print(ways)
    return len(ways)
    
def getSets(v, coins, memo):
    if v == 0:
        return {""}
    if v < 0:
        return None
    if v in memo:
        return memo[v]
    ways = set()
    for d in coins:
        dif = v - d
        if d > v or dif < minCoin or (dif in coins and dif != d):
            continue
        differenceWays = getSets(dif, coins, memo)
        for dway in differenceWays:
            dlist = (dway).split(",")
            dlist.append(str(d))
            dlist.sort()
            dstr = ",".join(dlist)
            ways.add(dstr)
    memo[v] = ways
    return ways
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    infile = open('coins_001.txt', 'r')

    nm = infile.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    coins = list(map(int, infile.readline().rstrip().split()))
    # print("coins", coins) 
    res = ways(n, coins)

    print(str(res) + '\n')

    # fptr.close()