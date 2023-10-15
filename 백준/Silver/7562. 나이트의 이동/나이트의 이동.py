import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    L = int(input())
    chess = [[0 for _ in range(L)] for _ in range(L)]
    visited = [[False for _ in range(L)] for _ in range(L)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    dx = [-2, -1,-2, -1, 1, 2, 1, 2 ]
    dy = [1, 2, -1, -2, -2, -1, 2, 1]
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = True
    t = 0
    while q:
        _list = q.popleft()
        x, y = _list[0], _list[1]
        visited[x][y] = True
        if visited[ex][ey] == True:
            print(chess[ex][ey])
            break
        for i in range(8):
            if 0 <= x + dx[i] < L and 0 <= y + dy[i] < L:
                if not visited[x+ dx[i]][y+ dy[i]]:
                    q.append([x + dx[i], y+ dy[i]])
                    visited[x + dx[i]][y+ dy[i]] = True
                    chess[x + dx[i]][y+ dy[i]] = chess[x][y] + 1