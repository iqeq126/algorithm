from collections import defaultdict
import sys
input, print = sys.stdin.readline, sys.stdout.write
n = int(input())
for _ in range(n):
    t = int(input())
    s = defaultdict(list)
    for i in range(t):
        clothes, type = input().split()
        s[type].append(clothes)
    res =  1
    for cloth in s:
        res *= (len(s[cloth]) + 1)
    print(f"{res-1}\n")