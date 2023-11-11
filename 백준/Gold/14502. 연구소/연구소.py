import sys
from collections import deque
input = sys.stdin.readline
XY =[[0,1], [0, -1], [-1,0], [1, 0]]
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
global res
res = 0
def bfs():
    lst = deque()
    global res
    cnt = 0
    subGraph = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                lst.append((i, j))
            subGraph[i][j] = graph[i][j]
    while lst:
        x, y= lst.popleft()
        for dx, dy in XY:
            X = dx + x
            Y = dy + y
            if (0<= X < N) and (0<= Y < M):
                if subGraph[X][Y] == 0:
                    subGraph[X][Y] = 2
                    lst.append((X,Y))
    for i in range(N):
        for j in range(M):
            if subGraph[i][j] == 0:
                cnt += 1
    res = max(res, cnt)
def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                # 백트레킹 처리
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0
wall(0)
print(res)