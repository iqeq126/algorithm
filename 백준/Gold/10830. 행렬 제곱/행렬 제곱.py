import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
N, B = map(int, input().split())
RowCol = [list(map(int, input().split())) for _ in range(N)]
result = [[RowCol[j][i] % 1000 for i in range(N)] for j in range(N)]
temp = [[0 for i in range(N)] for j in range(N)]
def SquareRowCol(a, b):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp[i][j] += a[i][k] * b[k][j]
                temp[i][j] %= 1000
    for i in range(N):
        for j in range(N):
            b[i][j], temp[i][j] = temp[i][j], 0
def func(num):
    while num > 0:
        if num % 2 == 1:
            SquareRowCol(RowCol, result)
        SquareRowCol(RowCol, RowCol)
        num //= 2
func(B-1)
for i in range(N):
    print(*result[i])