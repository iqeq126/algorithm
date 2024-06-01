import sys
sys.setrecursionlimit(10**5)
r, c = map(int, sys.stdin.readline().split())
res = 0
board = list(list(sys.stdin.readline().rstrip('\n')) for _ in range(r))


def is_valid(y, x):
    return 0 <= y < r and 0 <= x < c


def dfs(y, x):
    if x == c:
        return True

    for dy in (-1,0,1):
        ny = y+dy
        if is_valid(ny, x) and board[ny][x] == '.':
            board[ny][x] = 'x'
            if dfs(ny, x+1):
                return True
    return False


for y in range(r):
    res += dfs(y, 1)

print(res)