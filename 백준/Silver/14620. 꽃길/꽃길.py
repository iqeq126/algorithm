import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
costLst = [[0 for _ in range(N-2)] for _ in range(N-2)]
visited = [ [False for _ in range(N-2) ]for _ in range(N-2)]
for i in range(1, N-1):
    for j in range(1, N-1):
        costLst[i-1][j-1] = graph[i][j] + graph[i-1][j] + graph[i+1][j] + graph[i][j-1] + graph[i][j+1]
X = [-1, 1, 0, 0, 0]
Y = [0, 0,0, -1, 1]
global res
res = sys.maxsize

def dfs(x, y, cnt, cost):
    global res
    if cnt == 3:
        res = min(res, cost)
        return

    for t in range(5):
        if (0 <= x + X[t] < N-2 ) and ( 0 <=  y + Y[t] < N-2):
            visited[x+ X[t]][y+Y[t]] = True

    for i in range(N-2):
        for j in range(N-2):
            if visited[i][j]:
                continue

            condition = True
            for t in range(5):
                if (0 <= i + X[t] < N - 2) and (0 <= j + Y[t] < N - 2):
                    if visited[i + X[t]][j + Y[t]] == True:
                        condition = False

            if condition:
                dfs(i, j, cnt + 1, cost + costLst[i][j])

                for t in range(5):
                    if (0 <= i + X[t] < N-2) and (0 <= j + Y[t] < N-2):
                        visited[i + X[t]][j + Y[t]] = False

for i in range(N-2):
    for j in range(N-2):
        dfs(i, j, 1, costLst[i][j])
        for t in range(5):
            if (0 <= i + X[t] < N - 2) and (0 <= j + Y[t] < N - 2):
                visited[i + X[t]][j + Y[t]] = False
print(res)