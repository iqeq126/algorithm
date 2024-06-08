import sys
from collections import deque
input, print = sys.stdin.readline, sys.stdout.write
n, m = map(int, input().split())
lst = list(map(int,input().split()))
q = deque()
for i in range(n):
    if q and i == q[0][1] + m:
        q.popleft()
    while q and q[-1][0] > lst[i]:
        q.pop()
    q.append((lst[i], i))
    print(f"{q[0][0]} ")