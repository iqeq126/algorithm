import sys
from itertools import combinations_with_replacement
input, print = sys.stdin.readline, sys.stdout.write
n, m = map(int, input().split())
_list = list(map(int, input().split()))
_list.sort()
p = combinations_with_replacement(_list, m)
for i in p:
    print(" ".join(map(str, i)) + "\n")