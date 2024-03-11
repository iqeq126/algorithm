import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
dir_q = deque()
snake_q = deque()
dxy = [[1,0], [0,1],[-1,0],[0,-1] ]
board = [[0] * (N+1) for _ in range(N+1)]
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x][y] = 1
L = int(input())
for _ in range(L):
    time, direction = input().split()
    dir_q.append([int(time), direction])

x, y, count = 1, 2, 1
direction_handler = 1
board[1][1] = 2
snake_q.append([1,1])

while True:
    if not 1 <= x <= N or not 1 <= y <= N:
        break
    if board[x][y] == 2:
        break
    if dir_q:
        next_time, next_direction = dir_q[0]
        if count == next_time:
            if next_direction == 'L':
                direction_handler = ( direction_handler + 1) % 4
            elif next_direction == 'D':
                direction_handler = (direction_handler - 1) % 4
            dir_q.popleft()

    if board[x][y] == 0:
        snake_q.append([x, y])
        sx, sy = snake_q.popleft()
        board[sx][sy] = 0

    elif board[x][y] == 1:
        snake_q.append([x, y])

    board[x][y] = 2

    x += dxy[direction_handler][0]
    y += dxy[direction_handler][1]
    count += 1

print(count)