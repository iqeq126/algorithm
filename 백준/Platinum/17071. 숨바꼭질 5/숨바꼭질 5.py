import sys
from collections import deque
n, k = map(int, input().split())
MAX = 500_001
visited = [[-1, -1] for _ in range(MAX)]
def bfs(N):
    q = deque()
    q.append((N, 0))
    t = 0
    visited[N][0] = 0
    while q:
        for _ in range(len(q)):
            subin, sec = q.popleft()
            move = [subin+1, subin-1, subin*2]
            for m in move:
                if not ( 0 <= m < MAX): continue
                if visited[m][(sec+1)&1] != -1: continue
                q.append(((m, sec+1)))
                visited[m][(sec+1)&1] = sec+1
bfs(n)
res, second = -1, 0
for i in range(MAX):
    k += i
    if k >= MAX: break
    if visited[k][second&1] <= second:
        print(second)
        sys.exit()
    second += 1
print(-1)