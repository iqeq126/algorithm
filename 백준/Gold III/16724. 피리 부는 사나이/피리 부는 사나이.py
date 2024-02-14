import sys
load = {'D': (0, 1), 'L': (-1, 0), 'R':(1, 0), 'U': (0, -1)}
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().split())
street = [list(input().strip("\n")) for _ in range(N)]
result = [[0 for _ in range(M)] for _ in range(N)]
global safe_zone
safe_zone = 0
def dfs(x, y):
    global safe_zone
    result[y][x] = 1
    if result[y][x] == 0: result[y][x] = 1
    dx, dy = load[street[y][x]]
    X, Y  = x + dx, y + dy
    if 0 <= X < M and 0 <= Y < N:
        if result[Y][X] == 0: dfs(X, Y)
        if result[Y][X] == 1: safe_zone += 1
    result[y][x] = 2
    return
for i in range(N):
    for j in range(M):
        if result[i][j] == 0: dfs(j, i)
print(safe_zone)