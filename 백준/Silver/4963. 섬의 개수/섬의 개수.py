from collections import deque
import sys
input = sys.stdin.readline
dxy = [[0,1], [1,0], [-1,0], [0,-1], [1,1], [-1, -1], [1,-1], [-1,1]]
while True:
    m,n = map(int, input().split())
    if n==m==0: break
    island = [list(map(int, input().split())) for _ in range(n) ]
    visited = [ [False] * m for _ in range(n)]
    res = 0
    def bfs(x, y, result):
        q = deque()
        q.append([x, y])
        while q:
            cur_x, cur_y = q.popleft()
            if visited[cur_x][cur_y]:
                continue
            visited[cur_x][cur_y] = True
            for dx, dy in dxy:
                nx, ny = cur_x + dx, cur_y + dy
                if 0<= nx < n and 0<= ny < m:
                    if island[nx][ny] == 1:
                        q.append([nx, ny])
        return result+1
    for i in range(n):
        for j in range(m):
            if island[i][j] == 1 and not visited[i][j]:
                res = bfs(i, j, res)
    print(res)