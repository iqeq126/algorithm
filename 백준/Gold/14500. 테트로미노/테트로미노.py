import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[ False for _ in range(M)] for _ in range(N)]
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
global res
res = 0
def dfs(y, x , depth, local_res):
    global res
    if depth == 4:
        res = max(res, local_res)
        return

    for dx, dy in dxy:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if not visited[ny][nx]:
                if depth == 2:
                    visited[ny][nx] = True
                    dfs(y, x, depth+1, local_res + board[ny][nx])
                    visited[ny][nx] = False
                visited[ny][nx] = True
                dfs(ny, nx, depth + 1, local_res + board[ny][nx])
                visited[ny][nx] = False
for i in range(N):
    for j in range(M):
        # 백트래킹
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
print(res)