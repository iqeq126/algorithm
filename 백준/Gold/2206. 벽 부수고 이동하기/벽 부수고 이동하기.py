from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    dx = [1, 0, -1, 0]
    dy = [0, 1 ,0 ,-1]
    res = 2
    N, M = map(int, input().split())
    nm_map = [list(map(int, input().rstrip('\n'))) for _ in range(N)]
    visited = [[[False] * 2 for _ in range(M) ]for _ in range(N)]
    q = deque()
    q.append([0, 0, 1, 1])
    while q:
        x, y, dist, drill = q.popleft()
        if x == N-1 and y == M-1:
            return dist
        if visited[x][y][drill]:
            continue
        visited[x][y][drill] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if nm_map[nx][ny] == 0:
                    q.append([nx, ny, dist+1, drill])
                if nm_map[nx][ny] == 1 and drill == 1:
                    q.append([nx, ny, dist+1, drill-1])
    return -1
print(bfs())