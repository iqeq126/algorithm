import sys
MAX = 3001
sys.setrecursionlimit(MAX*2)
from collections import deque, defaultdict
input, print = sys.stdin.readline, sys.stdout.write
n = int(input())
q = deque()
isCycle = False
station = defaultdict(list)
visited = [False] * MAX
prev = [False] * MAX
cycle_list = [False] * MAX
dist = [0] * MAX
for _ in range(n):
    s, e = map(int, input().split())
    station[s].append(e)
    station[e].append(s)
def getCycle(now):
    global isCycle
    visited[now] = True
    for i in range(len(station[now])):
        if isCycle:
            return
        nxt = station[now][i]
        if not visited[nxt]:
            prev[nxt] = now
            getCycle(nxt)
        elif nxt != prev[now]:
            cycle_list[now], isCycle = True, True
            while now != nxt:
                cycle_list[prev[now]], now = True, prev[now]
            return



def bfs(q):
    init_dist = 0
    for init in range(1, n+1):
        if cycle_list[init]:
            visited[init] = True
            q.append((init, init_dist))
    while q:
        now, now_dist = q.popleft()
        visited[now] = True

        for nxt in station[now]:
            if visited[nxt]: continue
            dist[nxt] = now_dist + 1
            q.append((nxt, dist[nxt]))

getCycle(1)
visited = [False] * (n+1)
bfs(q)
for i in range(1, n):
    print(f"{dist[i]} ")
print(f"{dist[n]}\n")