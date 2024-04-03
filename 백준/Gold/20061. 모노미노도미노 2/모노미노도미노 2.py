import sys
input = sys.stdin.readline
n = int(input())
blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]
res = 0
bg = 0

def check_blue():
    res = 0
    for x in range(2, 6):
        count = 0
        for y in range(4):
            if blue[y][x]: count += 1
        if count == 4:
            delete_blue(x)
            res += 1
    return res

def delete_blue(x):
    while x > 0:
        for y in range(4):
            blue[y][x] = blue[y][x-1]
        x -= 1
    for i in range(4):
        blue[i][0] = 0

def move_blue(t, x, y=1):
    if t == 1 or t == 2:
        while True:
            if y + 1 > 5 or blue[x][y + 1]:
                blue[x][y] = 1
                if t == 2:
                    blue[x][y - 1] = 1
                break
            y += 1
    else:
        while True:
            if y + 1 > 5 or blue[x][y + 1] != 0 or blue[x + 1][y + 1] != 0:
                blue[x][y], blue[x + 1][y] = 1, 1
                break
            y += 1
    res = check_blue()
    for j in range(2):
        for i in range(4):
            if blue[i][j]:
                delete_blue(5)
                break
    return res

def check_green():
    res = 0
    for y in range(2, 6):
        count = 0
        for x in range(4):
            if green[y][x]: count += 1
        if count == 4:
            delete_green(y)
            res += 1
    return res
def delete_green(y):
    while y > 0:
        for x in range(4):
            green[y][x] = green[y-1][x]
        y -= 1
    for j in range(4):
        green[0][j] = 0
def move_green(t, x, y=1):
    if t == 1 or t == 3:
        while True:
            if y + 1 > 5 or green[y+1][x]:
                green[y][x] = 1
                if t == 3:
                    green[y-1][x] = 1
                break
            y += 1
    else:
        while True:
            if y + 1 > 5 or green[y+1][x] or green[y+1][x+1]:
                green[y][x], green[y][x+1] = 1, 1
                break
            y += 1

    res = check_green()

    for i in range(2):
        for j in range(4):
            if green[i][j]:
                delete_green(5)
                break
    return res

for _ in range(n):
    t, x, y = map(int, input().split())
    res += move_blue(t, x)
    res += move_green(t, y)

print(res)
for i in range(4):
    for j in range(4):
        if blue[i][j+2]: bg += 1
        if green[i+2][j]: bg += 1
print(bg)