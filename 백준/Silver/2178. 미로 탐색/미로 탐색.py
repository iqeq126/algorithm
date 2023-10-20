import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
res = 1
Matrix = [list(map(int, input().strip("\n"))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
cur = deque()
cur.append([0,0])
while cur:
    y, x = cur.popleft()
    if visited[y][x] == False:
        visited[y][x] = True
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < M and 0<= Y < N:
                if Matrix[Y][X] == 1:
                    Matrix[Y][X] = Matrix[y][x] +1
                    cur.append([Y,X])
print(Matrix[N-1][M-1])