import sys
from collections import deque
input = sys.stdin.readline
odd = [[-1,0], [0,-1], [1,0], [1,1], [0,1], [-1, 1]]
even = [[-1,-1], [0,-1], [1,-1], [1,0], [0,1], [-1, 0]]
X, Y = map(int, input().split())
illumination = [[0 for _ in range(X+2)] for _ in range(Y+2)]
outRange = [[False for _ in range(X+2)]for _ in range(Y+2)]
for i in range(1, Y+1):
    lst = list(map(int, input().split()))
    for j in range(1, X+1):
        illumination[i][j] = lst[j-1]

Q = deque([[0,0]])

while Q:
    y, x = Q.popleft()
    for k in range(6):
        if y % 2 == 0: # 짝수일 때
            dy, dx = y + even[k][0], x + even[k][1]
            if 0<= dy < Y+2 and 0<= dx < X+2:
                if outRange[dy][dx] == False and illumination[dy][dx] == 0:
                    outRange[dy][dx] = True
                    Q.append([dy, dx])
        else: # 홀수일 때
            dy, dx = y + odd[k][0], x + odd[k][1]
            if 0<= dy < Y+2 and 0<= dx < X+2:
                if outRange[dy][dx] == False and illumination[dy][dx] == 0:
                    outRange[dy][dx] = True
                    Q.append([dy, dx])
res = 0
dy, dx =0,0
for i in range(1, Y+1):
    for j in range(1, X+1):
        if illumination[i][j] == 0: continue
        for k in range(6):
            if i % 2 == 0: # 짝수일 때
                dy, dx = i + even[k][0], j + even[k][1]
            else: # 홀수일 때
                dy, dx = i + odd[k][0], j + odd[k][1]
            if outRange[dy][dx]: res +=1
print(res)