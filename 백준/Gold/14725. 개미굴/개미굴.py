import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
dictionary = dict()
def insert(dic, q):
    if q:
        item = q.popleft()
        if item not in dic:
            dic[item] = {}
        insert(dic[item], q)
    return
def printDictionary(dic, depth=0):
    if dic:
        for branch in sorted(dic.keys()):
            print("--" * depth + branch)
            printDictionary(dic[branch], depth+1)
    return
for i in range(N):
    q = deque(input().split())
    q.popleft()
    insert(dictionary, q)
printDictionary(dictionary)