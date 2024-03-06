import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
CHEESE, MELTING, OUTSIDE = 1, 2, 3
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
time = 0
init_cheese = 0
for i in range(N):
    init_cheese += cheese[i].count(1)
q = deque()
q.append([0, 0])
visited[0][0] = True
def setBlank():
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            X, Y = x + dx, y+ dy
            if 0 <= X < N and 0 <= Y < M:
                if visited[X][Y] == False and cheese[X][Y] != CHEESE:
                    visited[X][Y] = True
                    cheese[X][Y] = OUTSIDE
                    q.extend([[X,Y]])
def getTime(res_time=time, res=0):
    while True:
        # 내부-외부 연산
        setBlank()
        visit_flag = False
        # 치즈 녹이기
        for x in range(N):
            for y in range(M):
                if cheese[x][y] == CHEESE:
                    out_count = 0
                    for dx, dy in dxy:
                        X, Y = x + dx, y + dy
                        if 0 <= X< N and 0 <= Y < M and cheese[X][Y] == OUTSIDE:
                            visit_flag = True
                            out_count += 1
                    if out_count >= 1:
                        cheese[x][y] = MELTING
                        q.append([x, y])
        # 녹은 치즈 외부 처리
        if visit_flag:
            for x in range(N):
                for y in range(M):
                    if cheese[x][y] == MELTING:
                        cheese[x][y] = OUTSIDE
        res_time +=1
        cheese_num = 0
        for i in range(N):
            if CHEESE in cheese[i]:
                cheese_num += cheese[i].count(CHEESE)
        if cheese_num != 0:
            res = cheese_num
        if cheese_num == 0:
            return res_time, res
res = list(getTime(time, res=0))
print(f"{res[0]}\n{init_cheese}") if res[0] == 1 else print(*res, sep="\n")