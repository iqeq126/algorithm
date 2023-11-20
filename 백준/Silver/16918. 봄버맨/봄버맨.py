import sys
from collections import deque
input = sys.stdin.readline
R, C, N = map(int, input().split())
bomberList = [list(input().strip('\n')) for _ in range(R)]
Q = deque()
D = [[0, 1], [0, -1], [-1, 0], [1, 0]]
# N == 1일 때
if N == 1:
    # 그대로 출력
    for i in range(R): print(*bomberList[i], sep="")
# N % 2 == 2일 때
elif N % 2 == 0:
    # 전체를 O로 출력
    for _ in range(R):
        for _ in range(C):
            print("O", end="")
        print()
# N % 4 == 1일 때
elif N % 4 == 1:
    for y in range(R):
        for x in range(C):
            if bomberList[y][x] == "O":
                Q.append([y, x])

    while Q:
        qy, qx = Q.popleft()
        for dy, dx in D:
            X, Y = qx+dx, qy+dy
            if 0 <= X < C and 0 <= Y < R and bomberList[Y][X] == ".":
                bomberList[Y][X] = "O"
    for y in range(R):
        for x in range(C):
            if bomberList[y][x] == ".":
                Q.append([y, x])
    while Q:
        qy, qx = Q.popleft()
        for dy, dx in D:
            X, Y = qx+dx, qy+dy
            if 0 <= X < C and 0 <= Y < R:
                if bomberList[Y][X] == "O":
                    bomberList[Y][X] = "."
    for i in range(R): print(*bomberList[i], sep="")
# N % 4 == 3일 때
elif N % 4 == 3:
    for y in range(R):
        for x in range(C):
            if bomberList[y][x] == 'O':
                bomberList[y][x] = '.'
                Q.append([y, x])
            else:
                bomberList[y][x] = 'O'
    # 처음 설치된 폭탄을 포함한 주변의 폭탄을 .으로
    # 나머지 부분을 O로 출력
    #bomberList = [ [ "0" for _ in range(C)]for _ in range(R)]
    while Q:
        qy, qx = Q.popleft()
        for dy, dx in D:
            X, Y = qx+dx, qy+dy
            if 0 <= X < C and 0 <= Y < R:
                if bomberList[Y][X] == 'O':
                    bomberList[Y][X] = '.'
    for i in range(R): print(*bomberList[i], sep="")
