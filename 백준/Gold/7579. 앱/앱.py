import sys
input = sys.stdin.readline
N, M = map(int, input().split())

A = list(map(int, input().split())) # byte
C = list(map(int, input().split())) # cost
MAX = sum(C)+1
DP = [[0 for _ in range(MAX)] for _ in range(N+1) ]
res = sys.maxsize

for i in range(1, N+1):
    byte, cost = A[i-1], C[i-1]
    for j in range(MAX):
        if j < cost:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(byte + DP[i-1][j-cost], DP[i-1][j])

        if DP[i][j] >= M:
            res = min(res, j)
if M != 0:
    print(res)
else:
    print(0)