import sys
input = sys.stdin.readline
N = int(input())
_list = [list(map(int, input().split())) for _ in range(N)]
DP = [ [0 for _ in range(N)] for _ in range(N)]
DP[0][0] = 1
t = 0
for i in range(N):
    for j in range(N):
        I, J = i + _list[i][j], j + _list[i][j]
        if i == N-1 and j == N-1:
            break
        if I < N:
            DP[I][j] += DP[i][j]
            if _list[I][j] == 0:
                continue
        if J < N:
            DP[i][J] += DP[i][j]
            if _list[i][J] == 0:
                continue
print(DP[N-1][N-1])