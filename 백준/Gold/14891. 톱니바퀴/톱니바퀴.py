from collections import deque
gear = [deque(input()) for _ in range(4)]
n = int(input())
gear_move = [list(map(int, input().split())) for _ in range(n)]
left_teeth, right_teeth = 2, 6
def move_left(now, move):
    next, prev = now - 1, now + 1
    if now < 0:
        return
    if gear[now][left_teeth] != gear[prev][right_teeth]:
        move_left(next, -move)
        gear[now].rotate(move)
def move_right(now, move):
    next, prev = now + 1, now - 1
    if now > 3: return
    if gear[now][right_teeth] != gear[prev][left_teeth]:
        move_right(next, -move)
        gear[now].rotate(move)

for i in range(n):
    gear_number = gear_move[i][0]-1
    move_direction = gear_move[i][1]
    move_left(gear_number - 1, -move_direction)
    move_right(gear_number + 1, -move_direction)
    gear[gear_number].rotate(move_direction)

res = ''.join(format(int(gear[x][0]), 'b') for x in range(3,-1,-1))
print(int(res, 2))