from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    dx = [1, 0, -1, 0]
    dy = [0, 1 ,0 ,-1]
    N, M, K = map(int, input().split())
    nm_map = [list(map(int, input().rstrip('\n'))) for _ in range(N)]
    visited = [[ [False] * (M)  for _ in range(N)] for _ in range(K+1)]
    q = deque()
    q.append((0, 0, K))
    visited[K][0][0] = 1
    while q:
        x, y, drill = q.popleft()
        if x == N-1 and y == M-1:
            return visited[drill][x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if nm_map[nx][ny] == 1 and drill > 0 and visited[drill-1][nx][ny] == 0:
                    visited[drill-1][nx][ny] = visited[drill][x][y] + 1
                    q.append((nx, ny, drill-1))
                elif nm_map[nx][ny] == 0 and visited[drill][nx][ny] == 0:
                    visited[drill][nx][ny] = visited[drill][x][y] + 1
                    q.append((nx, ny, drill))
    return -1
print(bfs())