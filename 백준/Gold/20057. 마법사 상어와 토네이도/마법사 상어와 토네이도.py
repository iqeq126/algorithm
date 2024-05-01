import sys
input = sys.stdin.readline
n = int(input())
cy, cx = n//2, n//2
board = [list(map(int, input().split())) for _ in range(n)]
dyx = ((0,-1),(1,0),(0,1),(-1,0))
def hurricane(proportion):
    return list(reversed(list(zip(*proportion))))
s = [0 for _ in range(5)] * 4
s[0] = [  [0, 0,   0.02, 0,    0],
        [0, 0.1, 0.07, 0.01, 0],
        [0.05, 0, 0, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0, 0,   0.02, 0,    0]
        ]
s[1] = hurricane(s[0])
s[2] = hurricane(s[1])
s[3] = hurricane(s[2])
# 허리케인 이동 적용
a = ((2,1),(3,2),(2,3),(1,2))

def get():
    res = 0
    ny, nx = cy, cx
    direction, flag, diameter = 0, 2, 0
    prop = s[0]
    while True:
        if ny == nx == 0: break

        ny, nx = ny + dyx[direction][0], nx + dyx[direction][1]
        cur_sand, remained = board[ny][nx], board[ny][nx]
        board[ny][nx] = 0
        diameter += 1

        for dy in range(5):
            for dx in range(5):
                next_sand = int(cur_sand * prop[dy][dx])
                remained -= next_sand
                Y, X = ny + dy -2, nx + dx - 2
                if 0 <= Y < n and 0 <= X < n:
                    board[Y][X] += next_sand
                else:
                    res += next_sand

        aY, aX = ny + a[direction][0] - 2, nx + a[direction][1] - 2
        if 0 <= aY < n and 0 <= aX < n:
            board[aY][aX] += remained
        else:
            res += remained

        if diameter == flag // 2 or diameter == flag:
            direction = ( direction + 1 ) % 4
            prop = s[direction]
            if diameter == flag:
                diameter, flag = 0, flag + 2


    return res


print(get())