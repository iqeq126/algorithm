import sys
input = sys.stdin.readline
N, K = map(int, input().split())
S = [ list(map(int, input().split())) for i in range(N) ]
DP = [0 for _ in range(K+1) ]
s ,e,buf = -1, 0,0
value = 0
weight = 0
for i in range(N):
    DP[S[i][1]] = S[i][0]

print(DP[:20])