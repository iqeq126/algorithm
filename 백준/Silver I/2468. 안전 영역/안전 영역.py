import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N = int(input())
town = [list(map( int, input().split())) for _ in range(N)]
answer = 1
def dfs(x, y, rain, res):
    if town[y][x] > rain and visited[y][x] == False:
        visited[y][x] = True
        for i in range(4):
            X, Y = x + dx[i], y + dy[i]
            if 0 <= X < N and 0 <= Y < N:
                dfs(X, Y, rain, res)
        return res + 1
    else:
        return -1

for rain in range(101):
    visited = [[False for _ in range(N)] for _ in range(N)]
    res = 0
    for x in range(N):
        for y in range(N):
            t = dfs(x, y, rain, res)
            if t > res:
                res = t
    if res > answer:
        answer = res
print(answer)