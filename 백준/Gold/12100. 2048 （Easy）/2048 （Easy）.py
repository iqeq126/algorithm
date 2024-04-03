import sys, copy
sys.setrecursionlimit(10**8)
n = int(input())
global result
result = 0
_2048 = [list(map(int, input().split())) for _ in range(n)]
def move_left(board, n):
    for i in range(n):
        now = 0
        for j in range(1, n):
            if board[i][j] != 0:
                board[i][j], num = 0, board[i][j]

                if board[i][now] == 0:
                    board[i][now] = num

                elif board[i][now] == num:
                    board[i][now] *= 2
                    now += 1
                else:
                    now += 1
                    board[i][now] = num
    return board


def move_right(board, n):
    for i in range(n):
        now, j = n-1, n-1
        while j >= 0:
            if board[i][j] != 0:
                board[i][j], num = 0, board[i][j]

                if board[i][now] == 0:
                    board[i][now] = num

                elif board[i][now] == num:
                    board[i][now] *= 2
                    now -= 1
                else:
                    now -= 1
                    board[i][now] = num
            j-=1
    return board


def move_up(board, n):
    for j in range(n):
        now = 0
        for i in range(n):
            if board[i][j] != 0:
                board[i][j], num = 0, board[i][j]

                if board[now][j] == 0:
                    board[now][j] = num

                elif board[now][j] == num:
                    board[now][j] *= 2
                    now += 1
                else:
                    now += 1
                    board[now][j] = num
    return board


def move_down(board, n):
    for j in range(n):
        i, now = n - 1, n - 1
        while i >= 0:
            if board[i][j] != 0:
                board[i][j], num = 0, board[i][j]
                if board[now][j] == 0:
                    board[now][j] = num

                elif board[now][j] == num:
                    board[now][j] *= 2
                    now -= 1
                else:
                    now -= 1
                    board[now][j] = num
            i -= 1
    return board
def play_2048(cnt, board):
    global result
    if cnt == 5:
        for i in range(n):
            result = max(result, max(board[i]))
        return
    for i in range(4):
        copied_board = copy.deepcopy(board)
        if i == 0: play_2048(cnt + 1, move_left(copied_board, n))
        if i == 1: play_2048(cnt + 1, move_right(copied_board, n))
        if i == 2: play_2048(cnt + 1, move_up(copied_board, n))
        if i == 3: play_2048(cnt + 1, move_down(copied_board, n))

play_2048(0, _2048)
print(result)