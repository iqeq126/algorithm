import sys, heapq
from collections import deque, defaultdict
input, print = sys.stdin.readline, sys.stdout.write
N = int(input())
g = defaultdict(list)
dependency = [0] * (N+1)
build_time = [0] * (N+1)
total_build_time = [0] * (N+1)
for i in range(1, N+1):
    argv = deque(map(int, input().split()))
    build_time[i] = argv.popleft()
    while argv:
        argc = argv.popleft()
        if argc == -1:
            break
        g[argc].append(i)
        dependency[i] += 1

q = deque()
for i in range(1, N+1):
    if dependency[i] == 0:
        q.append(i)
        total_build_time[i] = build_time[i]

while q:
    now = q.popleft()
    for nxt in g[now]:
        total_build_time[nxt] = max(total_build_time[nxt],
                                    total_build_time[now] + build_time[nxt])
        dependency[nxt] -= 1
        if dependency[nxt] == 0:
            q.append(nxt)


for i in range(1, N+1):
    print(f"{total_build_time[i]}\n")