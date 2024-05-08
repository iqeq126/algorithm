import sys
input, print = sys.stdin.readline, sys.stdout.write
dp = [0, 1, 2, 4] + [0] * 1_000_005
MOD = 1_000_000_009
for i in range(4, 1000004):
    dp[i] = ( dp[i-1] + dp[i-2] + dp[i-3] ) % MOD
t = int(input())
for i in range(t):
    n = int(input())
    print(f"{dp[n]}\n")