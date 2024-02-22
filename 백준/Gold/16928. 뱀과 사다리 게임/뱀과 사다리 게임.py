import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
game_map = [ _ for _ in range(101) ]
visited = [ 0 for _ in range(101)]
for _ in range(N + M):
    s, e = map(int, input().split())
    game_map[s] = e
q = deque()
q.append(1)
while q:
    idx = q.popleft()
    for i in range(idx+1, idx+7):
        if i > 100: continue
        v = game_map[i]
        if visited[v] == 0:
            visited[v] = visited[idx] + 1
            q.append(v)
print(visited[100])