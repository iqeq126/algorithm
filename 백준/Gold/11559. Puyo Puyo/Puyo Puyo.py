import sys
from collections import deque
dxy = [(1,0), (-1,0), (0,-1),(0,1)]
input = sys.stdin.readline
board = [list(input().strip("\n")) for _ in range(12)]
result = 0
def puyopuyo(y, x, item, flag):
    puyo_field = []
    puyo_q = deque()
    puyo_q.append([y, x])
    puyo_field.append([y,x])
    visited[y][x] = True
    item_cnt = 1

    while puyo_q:
        cy, cx = puyo_q.popleft()
        for dy, dx in dxy:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < 12 and 0 <= nx < 6:
                if board[ny][nx] == item and not visited[ny][nx]:
                    visited[ny][nx] = True
                    puyo_q.append([ny, nx])
                    puyo_field.append([ny, nx])
                    item_cnt += 1
    if item_cnt >= 4:
        for i, j in puyo_field:
            board[i][j] = '.'
        flag = True
    return flag

while True:
    is_puyo = False
    visited = [[False] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                is_puyo = puyopuyo(i, j, board[i][j], is_puyo)
    for i in range(6):
        gravity_q = deque()

        for j in range(1, 13):
            if board[12-j][i] != '.':
                gravity_q.append(board[12-j][i])

        for j in range(1, 13):
            if gravity_q:
                board[12-j][i] = gravity_q.popleft()
            else:
                board[12-j][i] = '.'
    if is_puyo:
        result +=1
    else: break
print(result)