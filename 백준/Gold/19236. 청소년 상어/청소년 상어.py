from copy import deepcopy as copied
move = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1,1], [0,1], [-1,1]]
lst = [ list(map(int, input().split())) for _ in range(4) ]
board = [ [[] for __ in range(4)] for _ in range(4) ]
for i in range(4):
    for j in range(4):
        board[i][j] = [ lst[i][2*j]-1, lst[i][2*j+1]-1]
result = 0


def move_shark(sr, sc, res, board):
    global result
    res += ( 1 + board[sr][sc][0] )
    result = max(result, res)
    board[sr][sc][0] = -1
    cea = move_fish(sr, sc, board)
    sd = cea[sr][sc][1]
    for i in [1,2,3,4]:
        nr, nc = sr + move[sd][0]*i, sc + move[sd][1]*i
        if 0 <= nr < 4 and 0 <= nc < 4 and cea[nr][nc][0] != -1:
            move_shark(nr, nc, res, copied(cea))


def move_fish(sr, sc, cea):
    for target in range(16):
        fr, fc = -1, -1
        flag = True
        for r in range(4):
            for c in range(4):
                if flag:
                    if cea[r][c][0] == target:
                        fr, fc = r, c
                        flag = False
                        break
        if flag:
            continue
        target_direction = cea[fr][fc][1]
        for d in range(8):
            td = (target_direction + d) % 8
            tr, tc = fr+move[td][0], fc + move[td][1]
            if 0 <= tr < 4 and 0 <= tc < 4:
                if tr == sr and tc == sc:
                    continue
                cea[fr][fc][1] = td
                cea[fr][fc], cea[tr][tc] = cea[tr][tc], cea[fr][fc]
                break
    return cea


move_shark(0, 0, 0, board)
print(result)
