# https://regularmember.tistory.com/172

import sys
from collections import deque
input = sys.stdin.readline
horse = [[2,1], [2, -1], [-2, 1], [-2, -1], [1,2], [1,-2], [-1, 2], [-1, -2] ]
monkey = [[0,1], [0, -1], [1, 0], [-1, 0]]
k = int(input())
W, H  = map(int, input().split())
zoo = [list(map(int, input().split())) for _ in range(H)]
visited = [[[-1 for _ in range(k+1) ]for _ in range(W)] for _ in range(H) ]
# y, x, res, k
Q = deque([[0, 0, 0]])
res = sys.maxsize
visited[0][0][0] = 0
while Q:
    y, x, localK= Q.popleft()
    # 말처럼 움직이는 경우
    if localK < k:
        for hy, hx in horse:
            X, Y= hx + x, hy + y
            # 범위 체크
            if 0 <= X < W and 0 <= Y < H:
                # 장애물 확인
                if zoo[Y][X] == 1: continue
                # 방문 확인
                if visited[Y][X][localK+1] != -1: continue
                # 능력 사용시
                Q.extend([[Y, X, localK+1]])
                visited[Y][X][localK+1] = visited[y][x][localK] + 1

    for my, mx in monkey:
        X, Y = x + mx, y + my
        # 범위 체크
        if 0 <= X < W and 0 <= Y < H:
            # 장애물 확인
            if zoo[Y][X] == 1: continue
            # 방문 확인
            if visited[Y][X][localK] != -1: continue
            Q.extend([[Y, X, localK]])
            visited[Y][X][localK] = visited[y][x][localK] + 1
for i in range(k+1):
    if res > visited[H-1][W-1][i] > -1:
        res = visited[H-1][W-1][i]
if res == sys.maxsize:
    print(-1)
else:
    print(res)