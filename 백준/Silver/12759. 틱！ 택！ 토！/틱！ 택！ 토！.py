player = int(input())
win = 0
board = [[0 for _ in range(3)] for _ in range(3)]
def win_check(board):
    global win
    if win == 0:
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] == 0:
                    continue
                else:
                    win = board[i][0]
                    return
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j]:
                if board[0][j] == 0:
                    continue
                else:
                    win = board[0][j]
                    return
        if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
            if board[1][1] != 0:
                win = board[1][1]
                return
for i in range(9):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = player
    win_check(board)
    if player == 2:
        player -= 1
        continue
    else:
        player += 1
print(win)