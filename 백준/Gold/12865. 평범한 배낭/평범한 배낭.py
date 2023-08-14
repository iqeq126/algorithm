import sys
input = sys.stdin.readline
N, K = map(int, input().split())
S = [ list(map(int, input().split())) for i in range(N) ]
DP = [[0 for _ in range(K+1)] for _ in range(N+1) ]
s ,e,buf = -1, 0,0
value = 0
weight = 0
num = 0
S.sort(key=lambda S: S[1])
for i in range(1, N+1):
    for j in range(1, K+1):
        if S[i-1][0] > j:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-S[i-1][0]] + S[i-1][1])

print(DP[N][K])