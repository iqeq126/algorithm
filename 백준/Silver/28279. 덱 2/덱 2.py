import sys
from collections import deque
input, print = sys.stdin.readline, sys.stdout.write
N = int(input())
q = deque()
for _ in range(N):
    lst = list(map(int, input().split()))
    cmd = lst[0]
    if cmd == 1: q.appendleft(lst[1])
    if cmd == 2: q.append(lst[1])
    if cmd == 3: print(f"{q.popleft()}\n") if q else print("-1\n")
    if cmd == 4: print(f"{q.pop()}\n") if q else print("-1\n")
    if cmd == 5: print(f"{len(q)}\n")
    if cmd == 6: print("1\n") if not q else print("0\n")
    if cmd == 7: print(f"{q[0]}\n") if q else print("-1\n")
    if cmd == 8: print(f"{q[-1]}\n") if q else print("-1\n")