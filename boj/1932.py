import sys
input = sys.stdin.readline
N = int(input())
_list = [list(map(int, input().split())) for _ in range(N)]
DP = [[0 for _ in range(i+1)] for i in range(N)]
DP[0][0] = _list[0][0]
if N == 1:
    print(DP[0][0])
elif N > 1:
    DP[1][0] = DP[0][0] + _list[1][0]
    DP[1][1] = DP[0][0] + _list[1][1]
    if N > 2:
        for i in range(2, N):
            DP[i][0] = DP[i-1][0] + _list[i][0]
            for j in range(0, i):
                if j >= 1:
                    DP[i][j] = max(DP[i-1][j-1] + _list[i][j], DP[i-1][j] + _list[i][j])
            DP[i][i] = DP[i-1][i-1] + _list[i][i]
        print(max(DP[N-1]))
    else:
        print(max(DP[1][0], DP[1][1]))