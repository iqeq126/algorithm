import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
visited = set()
painting_num = 0
paint = [0]
papers = [list(map(int, input().split())) for _ in range(n)]
global res
res = 0
def dfs(y,x):
    global res
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    if not ( 0 <= y < n and 0 <= x < m): return False
    if (y, x) not in visited and papers[y][x] == 1:
        res += 1
        visited.add((y, x))
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            dfs(ny, nx)
        return True
    return False
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            paint.append(res)
            res = 0
print(len(paint)-1)
print(max(paint))