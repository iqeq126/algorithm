from collections import deque
import sys
dxy = [[1,0],[0,1],[-1,0],[0,-1]]
N, M = map(int, sys.stdin.readline().split())
map_info = [ list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [ [-1] * M for _ in range(N)]
x, y = 0, 0
for i in range(N):
    if 2 in map_info[i]:
        x, y = i, map_info[i].index(2)
        break
q = deque()
q.append([x, y, 0])
while q:
    cur_x, cur_y, dist = q.popleft()
    # visited[cur_x][cur_y] = dist
    for dx, dy in dxy:
        next_x, next_y = cur_x+dx, cur_y+dy
        if 0<=next_x<N and 0<= next_y < M:
            if map_info[next_x][next_y] == 0:
                visited[next_x][next_y] = 0
            elif map_info[next_x][next_y] == 1 and visited[next_x][next_y] == -1:
                q.append([next_x, next_y, dist + 1])
                visited[next_x][next_y] = dist+1
visited[x][y] = 0
for i in range(N):
    for j in range(M):
        if map_info[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()