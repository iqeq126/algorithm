import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
y1, x1, y2, x2 = map(int, input().split())
graph = list( input().rstrip() for _ in range(n))
MAX = 10 ** 6
min_dist = [[MAX for _ in range(m)] for _ in range(n)]
min_dist[y1-1][x1-1] = 0
q = [(0, y1-1, x1-1)]
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

while q:
    now_dist, y, x = heapq.heappop(q)
    if min_dist[y][x] < now_dist:
        continue

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            new_dist = now_dist + ( graph[ny][nx] != '0' )
            if new_dist < min_dist[ny][nx]:
                heapq.heappush(q, (new_dist, ny, nx))
                min_dist[ny][nx] = new_dist
print(min_dist[y2-1][x2-1])