import sys
sys.setrecursionlimit(10**4)
r, c = map(int, sys.stdin.readline().split())
res = 0
board = list(list(sys.stdin.readline().rstrip('\n')) for _ in range(r))


def is_valid(y, x):
    return 0 <= y < r and 0 <= x < c


def dfs(y, x):
    if x == c-1:
        return True

    nx = x+1
    for dy in (-1,0,1):
        ny = y+dy
        if is_valid(ny, nx) and board[ny][nx] == '.':
            board[ny][nx] = 'x'
            if dfs(ny, nx):
                return True
    return False


for y in range(r):
    res += dfs(y, 0)

print(res)