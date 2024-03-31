import sys
input = sys.stdin.readline
N = int(input())
dp = [0] * N
R = list(map(int, input().split()))
dp[0] = 0
if N > 1: dp[1] = min(R[0], R[1])
if N > 2:
    for i in range(2, N):
        dp[i] = min(dp[i - 2] + R[i-1], dp[i - 1] + R[i])
print(dp[-1])