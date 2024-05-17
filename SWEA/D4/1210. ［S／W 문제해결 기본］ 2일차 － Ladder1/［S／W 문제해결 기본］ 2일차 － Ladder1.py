from collections import deque
for tt in range(10):
    cnt = 10003
    res = 0
    n = int(input())
    q = deque()
    board = [ list(map(int, input().split())) for _ in range(100)]
    visited = [[10001 for _ in range(100)] for __ in range(100)]

    def dfs(player_y, player_x, status):
        move = ((-1, 0), (0,-1),(0,1))
        if player_y == 0:
            print(f"#{n} {player_x}")
            return
        tag = [False, False, False]
        flag = True
        for i in range(3):
            new_y, new_x = player_y+move[i][0], player_x+move[i][1]
            if 0 <= new_x < 100 and 0<= new_y < 100:
                if board[new_y][new_x] == 1:
                    tag[i] = True

        if tag[0] and ( not tag[1] ) and ( not tag[2] ):
            dfs(player_y-1, player_x, 'UP')

        if tag[0] and tag[1] and ( not tag[2] ):
            if status == 'UP':
                while board[player_y][player_x] == 1:
                    if (player_x -  1  >=
                            0):
                        player_x -= 1
                    else:
                        flag = False
                        break
                dfs(player_y, player_x+1, 'LEFT') if flag else dfs(player_y, player_x, 'LEFT')
            else:
                dfs(player_y - 1, player_x, 'UP')

        elif tag[0] and ( not tag[1] ) and tag[2]:
            if status == 'UP':
                while board[player_y][player_x] == 1:
                    if player_x +  1  < 100:
                        player_x += 1
                    else:
                        flag = False
                        break
                dfs(player_y, player_x-1, 'RIGHT') if flag else dfs(player_y, player_x, 'RIGHT')
            else:
                dfs(player_y - 1, player_x, 'UP')

    for i in range(100):
        if board[99][i] == 2:
            dfs(99, i, 'UP')
            break