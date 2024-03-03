route = [(1,0), (-1,0), (0,-1), (0,1), (1,1), (1,-1), (-1,1), (-1,-1)]
n = int(input())
mine_map = [list(input()) for _ in range(n)]
game_map = [list(input()) for _ in range(n)]
tag = False
mine = []
for i in range(n):
    for j in range(n):
        if mine_map[i][j] == '*':
            mine.append((i,j))
        if game_map[i][j] == 'x':
            if mine_map[i][j] == '*':
                tag=True
            dot = 0
            for ry, rx in route:
                I, J = i+ry, j + rx
                if 0 <= I < n and 0<= J <n:
                    if mine_map[I][J] == '*':
                        dot += 1
            game_map[i][j] = str(dot)
if tag:
    for my, mx in mine:
        game_map[my][mx] = '*'
for i in range(n):
    print(*game_map[i], sep='')