import sys
N, M = map(int, sys.stdin.readline().split())
lst = set()
res = set()
for _ in range(N):
    lst.add(input())
for _ in range(M):
    s = input()
    if s in lst:
        res.add(s)
print(len(res))
print(*sorted(res), sep="\n")