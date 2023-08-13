import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split())
tomato = [[[0 for _ in range(H)]for _ in range(M)] for _ in range(N)]
q = deque()
answer, t = 0, 0

for k in range(H):
    for i in range(N):
        _list = list(map(int, input().split()))
        for j in range(M):
                tomato[i][j][k] = _list[j]
                if _list[j] == 1:
                    q.append([i,j,k])
def bfs():
    dx = [ 1, 0, 0, -1, 0, 0 ]
    dy = [ 0, 1, 0, 0, -1, 0 ]
    dz = [ 0, 0, 1, 0, 0, -1 ]
    while q:
        _list = q.popleft()
        z, y, x = _list[0], _list[1], _list[2]
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nz < N and 0 <= ny < M and 0 <= nx < H:
                if tomato[nz][ny][nx] == 0:
                    tomato[nz][ny][nx] = tomato[z][y][x] + 1
                    q.append([nz, ny, nx])
bfs()
for i in range(N):
    for j in range(M):
        for k in range(H):
            if tomato[i][j][k] == 0:
                t = -1
            if t != -1 and answer < tomato[i][j][k]:
                answer = tomato[i][j][k]
if t == -1:
    print(t)
else:
    print(answer-1)