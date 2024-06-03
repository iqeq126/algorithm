import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n, m = map(int, input().split())
users = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    users[a].append(b)
    users[b].append(a)

def bfs(s):
    q = deque()
    q.append(s)
    while q:
        cur = q.popleft()
        for nxt in users[cur]:
            if visited[nxt] == 0 and s != nxt:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)

res = sys.maxsize
min_user_idx = 0
for i in range(1, n+1):
    visited = [0] * (n+1)
    bfs(i)
    local_res = sum(visited)
    if res > local_res:
        res = local_res
        min_user_idx = i

print(min_user_idx)
