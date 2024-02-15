import sys
input = sys.stdin.readline
lst = [list(map(int, input().split())) for _ in range(9)]
res = 0
for i in range(9):
    num = max(lst[i])
    if num > res:
        res = num

for i in range(9):
    for j in range(9):
        if lst[i][j] == res:
            print(res)
            print(i+1, j+1)
            sys.exit()