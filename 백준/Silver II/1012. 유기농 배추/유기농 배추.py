import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
T = int(input())

def bfs(lst, x, y):
    Q = deque()
    Q.append([x, y])
    while Q:
        x, y = Q.popleft()
        if (x, y) in visited:
            visited.remove((x, y))
            for data in range(4):
                X, Y = dx[data] + x, dy[data] + y
                if 0 <= X < N and 0 <= Y < M:
                    if lst[X][Y] == 1:
                        Q.append([X, Y])
for t in range(T):
    N, M, K =  map(int, input().split())
    _lst = [[0 for _ in range(M)] for _ in range(N)]
    visited = set()
    q = deque()
    res = 0
    for k in range(K):
        i, j = map(int, input().split())
        _lst[i][j] = 1
        q.append([i, j])
        visited.add((i, j))
    while q:
        x, y = q.popleft()
        if (x, y) not in visited:
            continue
        bfs(_lst, x, y)
        res+=1
    print(res)