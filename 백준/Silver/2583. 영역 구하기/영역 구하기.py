import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[1 for _ in range(n)] for __ in range(m)]
visited = [[False for _ in range(n)] for __ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 0


ans_list = [0]
index = 0

def dfs(y, x):
    global index
    if not visited[y][x] and graph[y][x] == 1:
        visited[y][x] = True
        ans_list[index] += 1
        if y < m-1:
            dfs(y + 1, x)
        if y > 0:
            dfs(y - 1, x)
        if x > 0:
            dfs(y, x - 1)
        if x < n-1:
            dfs(y, x + 1)

for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            dfs(i, j)
            ans_list.append(0)
            index += 1
ans_list.sort()
print(index)
print(*ans_list[1:])