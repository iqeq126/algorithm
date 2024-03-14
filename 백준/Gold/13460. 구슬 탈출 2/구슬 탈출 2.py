from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
# R, U, L, D = 0, 1, 2, 3
#dx = [1, -1, 0, 0]
#dy = [0, 0, -1, 1]
dxy = [ [0, 1], [1, 0], [-1, 0], [0, -1]]
res = 0
board = []
red_q, red_x, red_y = deque(), 0, 0
blue_q, blue_x, blue_y = deque(), 0, 0

for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[i][j] == 'R':
            red_x, red_y = i, j
        elif board[i][j] == 'B':
            blue_x, blue_y = i, j

def marble_move(x, y, dx, dy):
    move_count = 0
    nx, ny = x, y
    while board[nx+dx][ny+dy] != '#' and board[nx][ny] != 'O':
        nx, ny = nx+dx, ny+dy
        move_count += 1

    return nx, ny, move_count

def marble_exit():
    red_q.append([red_x, red_y])
    blue_q.append([blue_x, blue_y])
    count_q = deque()
    count_q.append(1)
    visited = set()
    visited.add((red_x, red_y, blue_x, blue_y))
    while count_q:
        rx, ry = red_q.popleft()
        bx, by = blue_q.popleft()
        count = count_q.popleft()
        if count > 10:
            continue
        for dx, dy in dxy:
            next_rx, next_ry, r_count = marble_move(rx, ry, dx, dy)
            next_bx, next_by, b_count = marble_move(bx, by, dx, dy)
            if board[next_bx][next_by] == 'O':
                continue

            if board[next_rx][next_ry] == 'O':
                return count

            if next_rx == next_bx and next_ry == next_by:
                if r_count > b_count:
                    next_rx, next_ry = next_rx - dx, next_ry - dy
                else:
                    next_bx, next_by = next_bx - dx, next_by - dy

            if (next_rx, next_ry, next_bx, next_by) not in visited:
                visited.add((next_rx, next_ry, next_bx, next_by))
                red_q.append([next_rx, next_ry])
                blue_q.append([next_bx, next_by])
                count_q.append(count+1)
    return -1

res = marble_exit()
print(res)