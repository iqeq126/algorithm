import sys
input = sys.stdin.readline
N = int(input())
lst = [int(input())for _ in range(N)]
lst.sort()
weight = 0
for i in range(N):
    if weight < (N-i) * lst[i]:
        weight = (N-i) * lst[i]
print(weight)