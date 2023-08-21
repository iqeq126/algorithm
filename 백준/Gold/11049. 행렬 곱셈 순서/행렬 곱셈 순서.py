import sys
input = sys.stdin.readline
N = int(input())
P = [ [0 for _ in range(N+2)] for _ in range(N+2)]
DP = [[0 for _ in range(N+2)] for _ in range(N+2)]
for i in range(1, N+1):
    P[i][0], P[i][1] = list(map(int, input().split()))
for r in range(2, N+1):
    for i in range(1, N-r+2):
        j = i + r-1
        DP[i][j] = sys.maxsize
        for k in range(i, j):
            val = DP[i][k] + DP[k+1][j] + P[i][0] * P[k][1] * P[j][1]
            DP[i][j] = min(val, DP[i][j])
print(DP[1][N])