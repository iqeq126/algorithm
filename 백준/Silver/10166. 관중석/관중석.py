import sys
input = sys.stdin.readline
N, M = map(int, input().split())
s = set()
for i in range(N, M+1):
    for j in range(1, i+1):
        s.add(i/j)
print(len(s))